import cv2
import mediapipe as mp
import serial
import time

#ser = serial.Serial('COM4', 9600, timeout = 1)
#time.sleep(2)

mp_Face_Detection = mp.solutions.face_detection

LABELS = ["Con_Mascarilla", "Sin_Mascarilla"]

# Read model 
Face_Mask = cv2.face.LBPHFaceRecognizer_create()
Face_Mask.read("Face_Mask_Model.xml")


def camera():

    cont_cm = 0
    cont_sm = 0
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    with mp_Face_Detection.FaceDetection(
            min_detection_confidence=0.5) as face_detection:
        
        while True:
            
            ret, frame = cap.read()
            if ret == False:break
            frame = cv2.flip(frame, 1)
            
            height, width,_ = frame.shape
            Frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            Results = face_detection.process(Frame_RGB)
            
            if Results.detections is not None:
                for detection in Results.detections:
                    xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                    ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                    w = int(detection.location_data.relative_bounding_box.width * width)
                    h = int(detection.location_data.relative_bounding_box.height * height)
                    
                    if xmin < 0 and ymin < 0:
                        continue
                    
                    #cv2.rectangle(frame, (xmin,ymin), (xmin + w, ymin + h),(0, 255, 0), 5) 
                    
                    Face_Image = frame[ymin : ymin + h, xmin : xmin + w]
                    Face_Image = cv2.cvtColor(Face_Image, cv2.COLOR_BGR2GRAY)
                    Face_Image = cv2.resize(Face_Image,(72,72), interpolation = cv2.INTER_CUBIC)
                   
                    Result = Face_Mask.predict(Face_Image)
                    #cv2.putText(frame, "{}".format(Result), (xmin, ymin - 5),1, 1.3, (210, 124, 176), 1, cv2.LINE_AA)
                    
                    if Result[1] < 150:
                        color = (0, 255, 0) if LABELS[Result[0]] == "Con_Mascarilla" else (0 ,0 ,255)
                        if Result[0] == 0:
                            cont_cm = cont_cm + 1;
                            print(cont_cm)
                            if cont_cm == 50:
                                #ser.write(b'O')
                                cv2.destroyAllWindows()
                                break
                        else:
                            cont_sm = cont_sm + 1;
                            print(cont_sm)
                            if cont_sm == 50:    
                                #ser.write(b'C')
                                cv2.destroyAllWindows()
                                break
                        cv2.putText(frame, "{}".format(LABELS[Result[0]]),(xmin, ymin - 25),2, 1, color, 1, cv2.LINE_AA)
                        cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h),color, 2)
                       
            cv2.imshow("Frame",frame)
            cv2.waitKey(1)
            
            if cont_sm == 50 or cont_cm == 50:
                break
                break
            
        cap.release()
        cv2.destroyAllWindows()  
            
        
#while True:
    
    #cad = ser.readline().decode('ascii')
    #print(len(cad))
    
    #if len(cad) != 0:
        #button = int(cad) + 10
        #print(button)
        #if int(cad) > 650:
           #ser.write(b'M')
           #camera()

#ser.close()
camera()