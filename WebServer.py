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
    cam = cv2.VideoCapture(cam_port) 
    
    # reading the input using the camera 
    result, image = cam.read() 
    
    # If image will detected without any error,  
    # show result 
    if result: 
        # saving image in local storage 
        cv2.imwrite("static/image.jpg", image) 
        status = "Success"
    
    # If captured image is corrupted, moving to else part 
    else: 
        status = "No image detected. Please! try again"

    return render_template('image.html', message=status)
