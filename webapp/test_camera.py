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
    d1 = cv2.absdiff(im1, im2)
    sum = d1.sum()
#   print('th=' + str(th) + ' : sum=' + str(sum))
    return (th < sum)


def save_image(image, filepath):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d %H%M%S')
    location=(460, 470)
    fontface=cv2.FONT_HERSHEY_PLAIN
    fontscale=1.0
    color=(0,255,0)
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
        if (True == is_moving(im1, im2, th)):
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
#   image = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    ret, image = cam.read()
    filename = 'main0.jpg'
    cv2.imwrite(SAVE_PATH + filename, image)
    print('take ' + filename)


def flame_sub(im1, im2, im3, th, blur):
    d1 = cv2.absdiff(im3, im2)
    d2 = cv2.absdiff(im2, im1)
    diff = cv2.bitwise_and(d1, d2)
    # 差分が閾値より小さければTrue
    mask = diff < th
    # 背景画像と同じサイズの配列生成
    im_mask = np.empty((im1.shape[0], im1.shape[1]), np.uint8)
    im_mask[:][:] = 255
    # Trueの部分（背景）は黒塗り
    im_mask[mask] = 0
    # ゴマ塩ノイズ除去
    im_mask = cv2.medianBlur(im_mask,blur)

    return  im_mask


def main_org():
    cam = cv2.VideoCapture(0)
    im1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while True:
        # フレーム間差分計算
        im_fs = flame_sub(im1, im2, im3, 5, 7)
#       cv2.imshow('Input',im2)
#       cv2.imshow('Motion Mask',im_fs)
        im1 = im2
        im2 = im3
        im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        key = cv2.waitKey(10)
        # Escキーが押されたら
        if key == 27:
            cv2.imwrite(SAVE_PATH + 'input.jpg', im3)
            cv2.imwrite(SAVE_PATH + 'frame_sub.jpg', im_fs)
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
