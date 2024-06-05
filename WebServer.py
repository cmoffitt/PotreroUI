from flask import Flask, render_template, request
# importing OpenCV library 
import cv2
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World from Potrero!</p>"

@app.route("/image") 
def serve_image(): 
    # initialize the camera 
    # If you have multiple camera connected with  
    # current device, assign a value in cam_port  
    # variable according to that 
    cam_port = 0

    capture = cv2.VideoCapture(cam_port)
    
    # TODO: Catch format / out of range exception here
    width = float(request.args.get('width'))
    height = float(request.args.get('height'))

    # Set the image width and height
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #print(cv2.getBuildInformation())

    # Read the input
    result, image = capture.read() 
    
    if result: 
        # Add current date and time text to image
        # describe the font type
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Get current date and time  
        date_time = str(datetime.datetime.now())
        
        # write the date time in the video frame
        image = cv2.putText(image, date_time, (10, 10), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)

        # saving image in local storage 
        cv2.imwrite("static/image.jpg", image) 
        status = "Success"
    
    else: 
        status = "No image detected. Please! try again"

    return render_template('image.html', message=status)
