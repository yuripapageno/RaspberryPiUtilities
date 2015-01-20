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
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript">
function go(qry) {
    $.ajax({
        url: 'camera_view.fcgi?q=' + qry,
        cache: false,
        success: function(html){
            $("#photos").empty();
            $("#photos").html(html);
        }
    });
}
</script>
<title>camera view</title>
</head>
<body>
<div id="photos">
"""

HTML_FOOTER = """
</div>
<form>
<input type="button" value="Reset" onclick="go('reset')" style="font-size:120%;">
<input type="button" value="Reload" onclick="go('reload')" style="font-size:120%;">
<br />
<br />
<br />
</form>
</body>
</html>
"""


def page():
    global FILEPATH
    global HTML_HEADER
    global HTML_FOOTER

    outstring = ''
    outstring += HTML_HEADER
    outstring += list()
    outstring += HTML_FOOTER
    return outstring


def list():
    filepathes = glob.glob(FILEPATH)
    filepathes.sort(
        cmp=lambda x, y: int(os.path.getmtime(x) - os.path.getmtime(y)),
        reverse=False)
    liststring = ''
    for filepath in filepathes:
        filename = filepath[filepath.rfind('/')+1:]
        liststring += '<a href=ramdisk/' + filename + ' class=\"highslide\" onclick=\"return hs.expand(this)\"><img src=\"ramdisk/' + filename + '\" width=\"320\" height=\"240\" class=\"flyer\" /></a><br><br>\n'
    return liststring


def reset():
    global FILEPATH
    filepathes = glob.glob(FILEPATH)
    for filepath in filepathes:
        os.remove(filepath)
    return list()


if __name__ == '__main__':
    print page()
