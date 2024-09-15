# To work with open cv need to import it.
import cv2

# will start off with the basics, loading an image.
image = cv2.imread('C:\Users\Silas\Desktop')

# checking if image was loaded successfully.

if image is None:
    print("Error: Image not tholakaling!")
else:
    print("Image was loaded successfully !")
