Face Recognition System
This Python script performs face recognition using the face_recognition library along with OpenCV. It compares the faces detected in a main image (e.g., "Elon Musk.jpg") with a test image (e.g., "Elon Test.jpg") to determine if they match

Dependencies
Make sure you have the following dependencies installed:

OpenCV (cv2)
NumPy (numpy)
face_recognition (face_recognition)
You can install face_recognition using pip:
pip install face_recognition

Usage
Place your main image (e.g., "Elon Musk.jpg") and test image (e.g., "Elon Test.jpg") in the ImagesBasic folder.
Run the script face_recognition.py.
The script will display both images with rectangles drawn around detected faces. It will also print the results of face comparison and the face distance.
Variables and Functions
imgElon, imgTest, imgBill: Variables to store the main image, test image, and Bill Gates image, respectively.
faceElonLoc, faceElonTestLoc: Face locations detected in the main image and test image, respectively.
encodeElonMain, encodeElonTest, encodeBillMain: Encodings of the main image, test image, and Bill Gates image, respectively.
results: Comparison results between the main image and the test image.
facedis: Face distance between the main image and the test image.
cv2.rectangle(): Draws rectangles around detected faces.
cv2.putText(): Adds text indicating face comparison results to the test image.
cv2.imshow(): Displays the main image and the test image.
Contributing
Feel free to contribute to this project by adding new features, improving code quality, or fixing bugs. Fork the repository, make your changes, and submit a pull request.
