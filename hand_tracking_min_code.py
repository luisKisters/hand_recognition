import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

pTime = 0
cTime = 0
# handLms = hand landmark

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # imgRGB = cv2.flip(imgRGB, 1)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm  in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # if id == 4:
                #     cv2.circle(img, (cx,cy), 25, (255,0,0), cv2.FILLED)
                cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
                cv2.putText(img,str(int(id)), (cx+8,cy+8), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0,0,255), 1)
                
                    
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    cTime = time.time()
    fps = 1/(cTime-pTime)          
    pTime = cTime
    
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2 , (255,0,255), 2) 
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    