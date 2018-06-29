'''
facechop.py

-Takes an image and detects a face in it.
-For each face, an image file is generated
    -the images are strictly of the faces
'''

import cv2

def facechop(image):
    facedata = "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)
    if len(faces)>0:
        for f in [faces[0]]:
            x, y, w, h = [ v for v in f ]
            # cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255))
            print([x,y,w,h])
            if ((y-int(h*.3)) > 0 ) & ( (x-int(w*.2))>0):
                sub_face = img[y-int(h*.3):y+int(h*1.2), x-int(w*.2):x+int(w*1.2)]
            else:
                sub_face = img[0:y+h,0:x+w]

            face_file_name = "faces/face_" + image
            print(face_file_name)
            cv2.imwrite(face_file_name, sub_face)

        # cv2.imshow(image, img)
    return

import glob
import os
for root, dirs, files in os.walk("testpics", topdown=True):
    for name in dirs:
        a = (os.path.join(root, name))
        if not os.path.exists('faces/face_'+ a):
            os.makedirs('faces/face_'+ a)
        imagePattern = a + "/"+"*.jpg"
        imgList=glob.glob(imagePattern)
        print(imgList)
        for img in imgList:
            if not os.path.exists('faces/face_'+ img):
                facechop(img)
                os.remove(img)
            else:
                os.remove(img)


# if __name__ == '__main__':
#     imagePattern = "testpics/*.JPG"
#     imagePattern2="testpics/*.jpg"
#     imgList=glob.glob(imagePattern)
#     imgList.append
#
#     print(imgList)
#     for img in imgList:
#         # facechop(img)
#         print(img)
#
#     # while(True):
#     #     key = cv2.waitKey(20)
#     #     if key in [27, ord('Q'), ord('q')]:
#     #         break
