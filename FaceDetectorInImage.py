import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("ImagesBasic/Elon Musk.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("ImagesBasic/Elon Test.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

imgBill = face_recognition.load_image_file("ImagesBasic/Bill Gates.jpg")
imgBill = cv2.cvtColor(imgBill,cv2.COLOR_BGR2RGB)

#now we will detect faces and the location of facial landmarks in the main image

faceElonLoc = face_recognition.face_locations(imgElon)[0]
encodeElonMain = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceElonLoc[3], faceElonLoc[0]), (faceElonLoc[1], faceElonLoc[2]), (255,0,255), 5)

#below we will do it for the test image

faceElonTestLoc = face_recognition.face_locations(imgTest)[0]
encodeElonTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceElonTestLoc[3], faceElonTestLoc[0]), (faceElonTestLoc[1], faceElonTestLoc[2]), (255,0,255), 5)

encodeBillMain = face_recognition.face_encodings(imgBill)[0]
#so these encodings are those 128 different measurements that we earlier discussed

results = face_recognition.compare_faces([encodeElonMain], encodeElonTest)
facedis = face_recognition.face_distance([encodeElonMain], encodeElonTest)
# print(results, facedis)

#this line below is to add result text to our image

cv2.putText(imgTest, f'{results} {round(facedis[0],2)}', (50,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,255), 2)

# These two below lines will print the image
cv2.imshow('Elon Musk', imgElon)

cv2.imshow('Elon Test', imgTest)

cv2.waitKey(0)

