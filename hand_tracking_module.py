import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = int(round(detectionCon))
        self.trackCon = int(round(trackCon))

        
        # static_image_mode = False,
        # max_num_hands = 2,
        # min_detection_conficence = 0.5,
        # min_tracking_confidence = 0.5
                
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                
        return img
                # for id, lm  in enumerate(handLms.landmark):
                #     # print(id,lm)
                #     h, w, c = img.shape
                #     cx, cy = int(lm.x*w), int(lm.y*h)
                #     print(id, cx, cy)
                #     # if id == 4:
                #     #     cv2.circle(img, (cx,cy), 25, (255,0,0), cv2.FILLED)
                #     cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
                #     cv2.putText(img,str(int(id)), (cx+8,cy+8), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0,0,255), 1)
                    
        
# cTime = time.time()
# fps = 1/(cTime-pTime)          
# pTime = cTime

# cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2 , (255,0,255), 2) 

# cv2.imshow("Image", img)
# cv2.waitKey(1)
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    img = detector = handDetector()

    while True:
        success, img = cap.read()
        detector.findHands(img)
        
        cTime = time.time()
        fps = 1/(cTime-pTime)          
        pTime = cTime
        
        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2 , (255,0,255), 2) 
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
    