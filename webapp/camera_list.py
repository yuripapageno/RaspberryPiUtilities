#!/usr/bin/pythonCGI
# -*- coding: utf8
import glob
import os

FILEPATH = '/run/shm/ramdisk/*.jpg'

HTML_HEADER = """
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="content-language" content="ja">
<meta http-equiv="content-script-type" content="text/javascript">
<link rel="stylesheet" type="text/css" href="highslide/highslide.css" />
<script type="text/javascript" src="highslide/highslide.js">
</script>
<script type="text/javascript">hs.graphicsDir = 'highslide/graphics/';
</script>
<title>camera view</title>
</head>
<body id="top">
"""

HTML_FOOTER = """
</body>
</html>
"""


def page():
    global FILEPATH
    global HTML_HEADER
    global HTML_FOOTER
    filepathes = glob.glob(FILEPATH)
    filepathes.sort(
        cmp=lambda x, y: int(os.path.getmtime(x) - os.path.getmtime(y)),
        reverse=False)

    outstring = ''
    outstring += HTML_HEADER

    for filepath in filepathes:
        filename = filepath[filepath.rfind('/')+1:]
        outstring += '<a href=ramdisk/' + filename + ' class=\"highslide\" onclick=\"return hs.expand(this)\"><img src=\"ramdisk/' + filename + '\" width=\"320\" height=\"240\" class=\"flyer\" /></a><br><br>\n'

    outstring += HTML_FOOTER

    return outstring


def reset():
    global FILEPATH
    filepathes = glob.glob(FILEPATH)
    for filepath in filepathes:
        os.remove(filepath)
    return page()


if __name__ == '__main__':
    print page()
