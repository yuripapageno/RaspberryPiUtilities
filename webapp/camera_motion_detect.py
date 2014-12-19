#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import datetime
import time

SAVE_PATH = '/run/shm/ramdisk/'


def is_moving(image1, image2, th):
    im1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    im2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
    diff = cv2.absdiff(im1, im2)
    allsum = diff.sum()
#   print('th=' + str(th) + ' : sum=' + str(sum))
    return th < allsum


def save_image(image, filepath):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d %H%M%S')
    location = (460, 470)
    fontface = cv2.FONT_HERSHEY_PLAIN
    fontscale = 1.0
    color = (0, 255, 0)
    cv2.putText(image, timestamp, location, fontface, fontscale, color)
    cv2.imwrite(filepath, image)


def main():
    save_no = 0
    save_max = 30
    cam = cv2.VideoCapture(0)
    imwidth = cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    imheight = cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    print('capture size:%dx%d' % (imwidth, imheight))
    th = imwidth * imheight * 255.0 * 0.03
    ret, im1 = cam.read()

    while True:
        ret, im2 = cam.read()
        # フレーム間差分計算
        if is_moving(im1, im2, th):
            filename = 'moving_%04d.jpg' % save_no
            save_no = (save_no + 1) % save_max
            save_image(im2, SAVE_PATH + filename)
            print('take ' + filename)
        im1 = im2
        key = cv2.waitKey(3000)
        # Escキーが押されたら
        if int(key) == 27:
            break
#       print('continue...')


def main0():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    filename = 'main0.jpg'
    cv2.imwrite(SAVE_PATH + filename, image)
    print('take ' + filename)


if __name__ == '__main__':
    main()
