#!/usr/bin/pythonCGI

from flup.server.fcgi import WSGIServer
import urlparse
import camera_list


def myapp(environ, start_response):
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
