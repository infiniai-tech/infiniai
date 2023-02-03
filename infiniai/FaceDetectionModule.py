import cv2
import mediapipe as mp
import time


class FaceDetector( ):
    def __init__(self, minDetectionConf=0.5):

        self.minDetectionConf = minDetectionConf

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(minDetectionConf)

    def findFaces(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results)
        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):

                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.FancyDraw(img, bbox)
                    # cv2.rectangle(img, bbox, (255,0,255), 5)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20),
                                cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 5)
        return img, bboxs

    def FancyDraw(self, img, bbox, length=30, thickness=15, rectThicknes=5):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h

        cv2.rectangle(img, bbox, (255, 0, 255), rectThicknes)

        # Top Left x,y
        cv2.line(img, (x, y), (x + length, y), (255, 0, 255), thickness)
        cv2.line(img, (x, y), (x, y + length), (255, 0, 255), thickness)

        # Top Right x1,y
        cv2.line(img, (x1, y), (x1 - length, y), (255, 0, 255), thickness)
        cv2.line(img, (x1, y), (x1, y + length), (255, 0, 255), thickness)

        # Bottom Left x,y1
        cv2.line(img, (x, y1), (x + length, y1), (255, 0, 255), thickness)
        cv2.line(img, (x, y1), (x, y1 - length), (255, 0, 255), thickness)

        # Bottom Right x1,y1
        cv2.line(img, (x1, y1), (x1 - length, y1), (255, 0, 255), thickness)
        cv2.line(img, (x1, y1), (x1, y1 - length), (255, 0, 255), thickness)

        return img


def main():
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
        cv2.waitKey(1)


if __name__ == "__main__":
    main( )