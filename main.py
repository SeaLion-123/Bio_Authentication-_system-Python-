import cv2
import os
import platform

# Set the image file name
image_filename = '1.jpg'

# Determine the platform and set the path accordingly
if platform.system() == 'Windows':
    image_path = os.path.join('C:\\', 'Users', 'Silas', 'Desktop', 'Bio_Authentication', image_filename)
else:
    image_path = os.path.join('/home', 'silas', 'Desktop', 'Bio_Authentication', image_filename)

# Load the image in color
image = cv2.imread(image_path)

# Load the image in grayscale
gray_scale = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Image not loaded! Check if the path is correct: {image_path}")
else:
    # A pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray_scale, scaleFactor=1.1, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save and display the result
    output_filename = os.path.join('detected_faces.jpg')
    cv2.imwrite(output_filename, image)
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
