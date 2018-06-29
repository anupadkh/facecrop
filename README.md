# facecrop

This project is not the original version.

I just made changes to the file so that we can extract the required image size for an ID Card.
Note: It can't be used for extracting more than one photo.
Also sometimes dimensions could be a problem to properly recognize the faces.

# Getting started:
Just put your images in testpics folder.

Just check if following dependencies are met:
1. cv2
otherwise do:
pip3 install python-cv2

if you are training a dataset for face recognition use:
opencv_face_recognition
It can be used to train your faces using webcam.

to satisfy the requirements,
run:

pip3 install -r opencv_face_recognition/requirements.txt

