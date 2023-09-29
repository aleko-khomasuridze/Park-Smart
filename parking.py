# Import necessary libraries
import cv2 as cv           # OpenCV for computer vision tasks
import pickle              # For serializing and deserializing Python objects
import time                # For time-related functions
import numpy as np         # NumPy for numerical operations
from random import randint # To generate random numbers

# Initialize lists to store parking space information
space_odd  = []  # To store odd-numbered parking spaces
space_even = []  # To store even-numbered parking spaces

A_odd  = []      # To store the areas of odd-numbered parking spaces
A_even = []      # To store the areas of even-numbered parking spaces

# Initialize video capture from the default camera (0)
vid = cv.VideoCapture(0)

# Set video capture dimensions (width and height)
vid.set(3, 1280)  # Set width to 1280 pixels
vid.set(4, 720)   # Set height to 720 pixels

# Define the text for vacant parking spaces (converted to uppercase)
text = 'vacant'.upper()

# Initialize lists to store parking space coordinates (x and y)
cx = []  # X-coordinates of parking spaces
cy = []  # Y-coordinates of parking spaces

# Load the parking map image as a frame
frame = cv.imread("parkingMap.jpg")

# Define coordinates and dimensions for odd and even parking spaces
odd_parking  = []  # Stores colors for odd-numbered parking spaces
even_parking = []  # Stores colors for even-numbered parking spaces

odd_value =  []    # Stores statuses (vacant/busy) for odd-numbered parking spaces
even_value = []    # Stores statuses (vacant/busy) for even-numbered parking spaces
# Define coordinates and dimensions for odd-numbered parking spaces
odd_x  = (5,   180)            # X-coordinates range for odd parking spaces
odd_y  = (100, 200)            # Y-coordinates range for odd parking spaces
odd_WH = (odd_x[1] - odd_x[0], odd_y[1] - odd_y[0])  # Calculate width and height for odd parking spaces

# Define coordinates and dimensions for even-numbered parking spaces
even_x = (5,   180)            # X-coordinates range for even parking spaces
even_y = (390, 490)            # Y-coordinates range for even parking spaces

# Function to initialize parking spaces with a given color
def initParking(color):
    for i in range(5):
        # Append the specified color to both odd and even parking spaces
        even_parking.append(color)
        odd_parking.append(color)

        # Initialize parking space statuses as 'vacant' (converted to uppercase)
        odd_value.append("vacant".upper())
        even_value.append("vacant".upper())

# Function to draw a parking space box on the frame
def drawBox(k1, k2, l, color, frame):
    # Draw the lines to create the parking space box
    cv.line(frame, (k1[0], k1[1]), (k1[0]+l, k1[1]), color, 2)
    cv.line(frame, (k1[0], k1[1]+l), (k1[0], k1[1]), color, 2)
    cv.line(frame, (k2[0], k1[1]), (k2[0]-l, k1[1]), color, 2)
    cv.line(frame, (k2[0], k1[1]+l), (k2[0], k1[1]), color, 2)
    cv.line(frame, (k1[0], k2[1]), (k1[0]+l, k2[1]), color, 2)
    cv.line(frame, (k1[0], k2[1]-l), (k1[0], k2[1]), color, 2)
    cv.line(frame, (k2[0], k2[1]), (k2[0]-l, k2[1]), color, 2)
    cv.line(frame, (k2[0], k2[1]-l), (k2[0], k2[1]), color, 2)

    # Calculate the center of the parking space
    m1 = ((k1[0]+k2[0])//2, (k1[1]+k2[1])//2)

    # Draw a rectangle for displaying text (status) within the parking space
    cv.rectangle(frame, (m1[0]+55, m1[1]-30), (m1[0]+85, m1[1]+30), color, 2)
    
    # Draw filled rectangles for better text visibility
    cv.rectangle(frame, (k1[0]+3, k2[1]+5+3), (k1[0]+90+3, k2[1]+33), (color[0]-35, color[1]-35, color[2]-35), cv.FILLED)
    cv.rectangle(frame, (k1[0], k2[1]+5), (k1[0]+90, k2[1]+30), color, cv.FILLED)


def drawOdd(x, y, frame1, frame2):
    """
    Draw odd-numbered parking spaces on the frame.

    Parameters:
        x (tuple): X-coordinate range for parking spaces.
        y (tuple): Y-coordinate range for parking spaces.
        frame1 (numpy.ndarray): Original frame for visualization.
        frame2 (numpy.ndarray): Processed frame for parking space detection.
    """
    for i in range(5):
        # Draw parking space boundary on the frame
        drawBox((x[0]*(i+1) + x[1]*i, y[0]), ((i+1)*(x[0]+x[1]), y[1]), 25, odd_parking[i], frame)
        
        # Extract and store the region corresponding to the parking space
        space_odd.insert(i, frame2[y[0]:y[1], x[0]*(i+1) + x[1]*i:(i+1)*(x[0]+x[1])])
        
        # Display parking space images for specific indices
        if i+1 in [2, 5, 6, 9]:
            cv.imshow("car"+str(i), space_odd[i])
        
        # Count the number of nonzero pixels in the parking space
        A_odd.insert(i, cv.countNonZero(space_odd[i]))
        
        # Display parking space status (e.g., "vacant" or "busy") on the frame
        cv.putText(frame1, str(odd_value[i]), (x[0]*(i+1) + x[1]*i + 5, y[1]+25), cv.FONT_HERSHEY_PLAIN, 1.2, (0xFF, 0xFF, 0xFF), 2)

def drawEven(x, y, frame1, frame2):
    """
    Draw even-numbered parking spaces on the frame.

    Parameters:
        x (tuple): X-coordinate range for parking spaces.
        y (tuple): Y-coordinate range for parking spaces.
        frame1 (numpy.ndarray): Original frame for visualization.
        frame2 (numpy.ndarray): Processed frame for parking space detection.
    """
    for i in range(5):
        # Draw parking space boundary on the frame
        drawBox((x[0]*(i+1) + x[1]*i, y[0]), ((i+1)*(x[0]+x[1]), y[1]), 25, even_parking[i], frame)
        
        # Extract and store the region corresponding to the parking space
        space_even.insert(i, frame2[y[0]:y[1], x[0]*(i+1) + x[1]*i:(i+1)*(x[0]+x[1])])
        
        # Display parking space images for specific indices
        if i+1 in [2, 5, 6, 9]:
            cv.imshow("car"+str(i+6), space_even[i])
        
        # Count the number of nonzero pixels in the parking space
        A_even.insert(i, cv.countNonZero(space_even[i]))
        
        # Display parking space status (e.g., "vacant" or "busy") on the frame
        cv.putText(frame1, str(even_value[i]), (x[0]*(i+1) + x[1]*i + 5, y[1]+25), cv.FONT_HERSHEY_PLAIN, 1.2, (0xFF, 0xFF, 0xFF), 2)

# Initialize parking spaces with the specified color
initParking((255, 143, 5))  # The color (255, 143, 5) corresponds to a shade of orange

# Open a text file named "parkingMap.txt" in append mode
f = open("parkingMap.txt", 'a')

# Continuously process frames from the video capture
while True:
    ret, frame = vid.read()  # Read a frame from the video capture

    imgGray  = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    imgBlure = cv.GaussianBlur(imgGray, (3, 3), 1)    # Apply Gaussian blur for noise reduction
    imgThreshold = cv.adaptiveThreshold(imgBlure, 255, 
                    cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)  # Apply adaptive thresholding
    imgMedium = cv.medianBlur(imgThreshold, 5)        # Apply median blur for smoothing
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv.dilate(imgMedium, kernel, iterations=1)  # Apply dilation for better contour detection

    # Draw odd-numbered parking spaces on the frame
    drawOdd(odd_x, odd_y, frame, imgDilate)

    # Draw even-numbered parking spaces on the frame
    drawEven(even_x, even_y, frame, imgDilate)

    # Count the number of nonzero pixels in the third odd parking space (index 2)
    A002 = cv.countNonZero(space_odd[2])
    print(A002)

    # Modify parking space colors and statuses (for illustration purposes)
    # r1, r2 = randint(1, 4), randint(1, 4)
    # even_parking[r1] = (98, 41, 255)
    # odd_parking[r2] = (98, 41, 255)
    # even_value[r1] = "bussy".upper()
    # odd_value[r2] = "bussy".upper()

    # Update parking space statuses based on the number of nonzero pixels
    for i in range(5):
        if A_odd[i] > 200:
            odd_parking[i] = (98, 41, 255)  # Color for a "busy" parking space
            odd_value[i] = "busy".upper()  # Update status as "busy"
        else:
            odd_parking[i] = (255, 143, 5)  # Color for a "vacant" parking space
            odd_value[i] = "vacant".upper()  # Update status as "vacant"

        if A_even[i] > 200:
            even_parking[i] = (98, 41, 255)  # Color for a "busy" parking space
            even_value[i] = "busy".upper()  # Update status as "busy"
        else:
            even_parking[i] = (255, 143, 5)  # Color for a "vacant" parking space
            even_value[i] = "vacant".upper()  # Update status as "vacant"

    # Open the text file "parkingMap.txt" in read/write mode and truncate its content
    f = open("parkingMap.txt", 'r+')
    f.truncate(0)

    # Write parking space statuses to the text file
    for i in range(10):
        if i < 5:
            f.write(odd_value[i] + ':')
        else:
            f.write(even_value[i-5] + ':')

    f.write('\n')

    # Display the frame with parking spaces
    frame75 = frame[0:620, 0:940]
    imgDilate = imgThreshold[0:620, 0:940]
    cv.imshow('frame75', frame75)  # Display the frame with parking spaces

    # Check for the 'q' key press to exit the loop
    if cv.waitKey(1) == 0xFF & ord('q'):
        break

# Release the video capture and close OpenCV windows
vid.release()
cv.destroyAllWindows()
