# import cv2
# import os
# import platform

# # Set the image file name
# image_filename = 'Multiple_faces.jpg'

# # Determine the platform and set the path accordingly
# if platform.system() == 'Windows':
#     image_path = os.path.join('C:', 'Users', 'Silas', 'Desktop', 'Bio_Authentication', image_filename)
# else:
#     image_path = os.path.join('/home', 'silas', 'Desktop', 'Bio_Authentication-_system-Python-', image_filename)

# # Load the image in color
# image = cv2.imread(image_path)

# # Load the image in grayscale
# gray_scale = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # Check if the image was loaded successfully
# if image is None:
#     print(f"Error: Image not loaded! Check if the path is correct: {image_path}")
# else:
#     # A pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     # Detect faces in the grayscale image
#     faces = face_cascade.detectMultiScale(gray_scale, scaleFactor=1.1, minSize=(30, 30))

#     # Draw rectangles around detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     # Save and display the result
#     cv2.imwrite('detected_faces.jpg', image)
#     cv2.imshow('Face Detection', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
import cv2

# A pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to capture video from any available camera (camera 0 is default)
def detect_faces_from_camera():
    # Open a connection to the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the frame with detected faces
        cv2.imshow('Real-Time Face Detection', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the face detection function
detect_faces_from_camera()

