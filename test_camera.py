#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

SAVE_PATH = '/run/shm/ramdisk/'


def is_moving(image1, image2, th):
    im1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    im2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
    d1 = cv2.absdiff(im1, im2)
    sum = d1.sum()
    print('th=' + str(th) + ' : sum=' + str(sum))
    return (th < sum)


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
        if (True == is_moving(im1, im2, th)):
            filename = 'moving_%04d.jpg' % save_no
            save_no = (save_no + 1) % save_max
            cv2.imwrite(SAVE_PATH + filename, im2)
            print('take ' + filename)
        im1 = im2
        key = cv2.waitKey(3000)
        # Escキーが押されたら
        if key == 27:
            break
#       print('continue...')


def main0():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    if ret:
        filename = 'main0.jpg'
        cv2.imwrite(SAVE_PATH + filename, image)
        print('take ' + filename)
    else:
        print('capture error.')


if __name__ == '__main__':
    main()
