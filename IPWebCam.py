import urllib.request
import cv2
import numpy as np


url="http://192.168.43.1:8080/shot.jpg"

while True:


    imgResponse = urllib.request.urlopen(url)


    imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)


    img = cv2.imdecode(imgNp,-1)



    cv2.imshow("IPWebcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
