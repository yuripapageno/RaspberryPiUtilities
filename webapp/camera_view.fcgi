#!/usr/bin/pythonCGI

from flup.server.fcgi import WSGIServer
import urlparse
import camera_list
from common_logging import Logger

_logger = Logger('camera_view.log')


def myapp(environ, start_response):
    _logger.info('accessed from :' + str(environ['REMOTE_ADDR']))
#    for key, value in environ.iteritems():
#        _logger.debug('#' + key + ' :' + str(value))
    test = False
    if test:
        start_response('200 OK', [('Content-Type', 'text/plain')])
        qs = urlparse.parse_qs(environ['QUERY_STRING'])
        if 'q' in qs:
            return ['q : ' + qs['q'][0]]
        else:
            return ['no query...']
    start_response('200 OK', [('Content-Type', 'text/html')])
    qs = urlparse.parse_qs(environ['QUERY_STRING'])
    if 'q' in qs:
        if qs['q'][0] == 'reset':
            return [camera_list.reset()]
        else:
            return [camera_list.page()]
    else:
        return [camera_list.page()]
#    return [camera_list.page()]


if __name__ == '__main__':
    WSGIServer(myapp).run()
