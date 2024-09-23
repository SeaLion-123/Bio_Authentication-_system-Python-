# To work with open cv need to import it.
import cv2
# will start off with the basics, loading an image.
image = cv2.imread('C:\Users\Silas\Desktop\Multiple_faces.JPG',)
#This is a gray scale vision of the image.
gray_scale = cv2.imread('/home/wtc/Downloads/1722328614790.jpeg', cv2.IMREAD_GRAYSCALE)
# checking if image was loaded successfully.
if image is None:
    print("Error: Image not tholakaling!")
else:
    # print("Image was loaded successfully !")
    # cv2.imshow("Image Wndow", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #A model detection that comes pre-trained.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_scale, scaleFactor=1.1, minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imwrite('detected_faces.jpg',image)
        cv2.imshow('Face Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

