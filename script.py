import cv2
import numpy as np

def compare_images( "C:\Users\Dr. Joan\image compare project\test1.jpg", "C:\Users\Dr. Joan\image compare project\TEST2.jpg"):
    # Load the two AI-generated images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Resize the images to the same size (if needed)
    image1 = cv2.resize(image1, (400, 400))
    image2 = cv2.resize(image2, (400, 400))

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate the difference between the two images
    diff = cv2.absdiff(gray1, gray2)

    # Save the difference image
    cv2.imwrite('difference.png', diff)
    return 'difference.png'