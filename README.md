# infiniai





This is a Computer Vision package that makes it easy to run Image &amp; Video processing at scale. At the core it uses [OpenCV](https://github.com/opencv/opencv) and [Mediapipe](https://github.com/google/mediapipe) libraries.

## Installation
You can  simply use pip to install the latest version of infiniai.

`pip install infiniai`

<hr>

###  Face Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/infiniai-tech/infiniai/blob/main/Results/facedetection.png">
</p>

<pre>
from infiniai.FaceDetectionModule import FaceDetector
import cv2
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = FaceDetector( )
while True:
    success, img = cap.read( )
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    cTime = time.time( )
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>

<hr>

### Hand Tracking

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/infiniai-tech/infiniai/blob/main/Results/handtracking.png">
</p>

<pre>
from infiniai.HandTrackingModule import handDetector
import cv2
import time
import infiniai.HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    PosList = detector.findPosition(img)
    if len(PosList) != 0:
        print(PosList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
</pre>

 

<hr>

### Pose Estimation

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/infiniai-tech/infiniai/blob/main/Results/pose.png">
</p>

<pre>
from infiniai.PoseEstimationModule import poseDetector
import cv2
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = poseDetector()

while True:

    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time( )
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>


<hr>

### Face Mesh Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/infiniai-tech/infiniai/blob/main/Results/facemesh.png">
</p>

<pre>
from infiniai.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>


