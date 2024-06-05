from flask import Flask, render_template
# importing OpenCV library 
import cv2

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
    
    width = request.args.get('width')
    height = request.args.get('height')

    # Set the image width and height
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #print(cv2.getBuildInformation())

    # Read the input
    result, image = capture.read() 
    
    if result: 
        # saving image in local storage 
        cv2.imwrite("static/image.jpg", image) 
        status = "Success"
    
    else: 
        status = "No image detected. Please! try again"

    return render_template('image.html', message=status)
