# Import the eel library
import eel

# Initialize eel with the "web" directory where HTML and other web files are located
eel.init("web")

# Initialize an empty variable to store data
data = ''

# Read the content of the "parkingMap.txt" file and store it in the 'data' variable
with open("parkingMap.txt") as file:
    data = file.readline().strip()

# Print the data read from the file
print(data)

# Define an exposed function that can be called from JavaScript in the web page
@eel.expose
def sendData():
    print("sent data")
    return data  # Return the data to the JavaScript function

# Start the eel app with the "main.html" file as the main web page
eel.start("main.html")
