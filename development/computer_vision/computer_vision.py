

# Libraries to import
import cv2
import numpy as np


class Computer_vision():
    """Library for rendering and object detection on a image or a video:

    1. Resize an image                      = resize_image()
    2. Detect color range on video          = detect_colorRange()
    3. Detect and count objects on video    = 

    """


    # Instance of the 'OpenCV' class. 
    def __init__(self):
        pass


############################################################################################

    def resize_image(self, path=str, *args):
        """Resize image with percentage or fixed dimensions.
        Percentage and fixed dimensions can both downscale and upscale.

        Args:
            path - file path to image. [datatype: string]
            *args - One argument is for percentage. [datatype: integer or float]
            or
            *args - Two arguments is for fixed dimensions(width, height). [datatype: (interger, integer)]

        Returns:
            Display resized image in a separate window.
        """

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        print('Original Dimensions : ',img.shape)

        if len(args) == 1:
            try:
                # Calculate new dimensions
                width = int(img.shape[1] * args[0] / 100)   
                height = int(img.shape[0] * args[0] / 100)
                dim = (width, height)
                
                # resize image
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                
                cv2.imshow(f"Resized image: {resized.shape}", resized)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except:
                print(f"Percentage resizing failed with image: {path}")

        if len(args) == 2:
            try:
                # width and height
                dim = (args[0], args[1])
    
                # resize image
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                
                cv2.imshow(f"Resized image: {resized.shape}", resized)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except:
                print(f"Fixed dimension resizing failed with image: {path}")

        if len(args) < 2:
            print("[Resize image *args] An error occurred due to many arguments.")


############################################################################################

    def detect_colorRange(self, scr, *args, kernel=None):
        """Detect specific colors from a video. Will bound the area of the specific colors with a green box. 

        Press 'Esc' to close program. 

        Args:
            scr - source of videofeed. [datatype: integer]
                    0: Means first camera or webcam.
                    1: Means second camera or webcam.
                Or pass a path to a video file. [datatype: string]

            *args - specified color range to isolate.
                First: Low bound of color range in B,G,R order. [datatype: list]
                Second: Upper bound of color range in B,G,R order. [datatype: list]
            
            kernel - Default: numpy.ones((5 ,5), numpy.uint8)
                Customized matrix has to be a numpy array. [datatype: unsigned 8 bit integer(uint8)] 
        """

        cap = cv2.VideoCapture(scr)
        
        if kernel == None:
            kernel = np.ones((5 ,5), np.uint8)
        else:
            kernel = kernel

        while(cap.isOpened()):          # Returns True if video capturing has been initialized already

            ret, frame = cap.read()     # ret is a boolean variable that returns true if the frame is available.

            if ret==True:

                # Lower and upper bound of color [B, G, R]
                lower_color = np.array(args[0])       
                upper_color = np.array(args[1]) 

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # Convert frame to HSV
                
                mask = cv2.inRange(hsv, lower_color, upper_color)   # Turn color range white and the rest black
                
                opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   # Reduce the noise on frame

                x, y, w, h = cv2.boundingRect(opening)  # Extract coordinates, width and height of 
            
                cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 3)  # Create rectangle and center dot

                cv2.imshow('Color detection', frame) # Display video with rectangle and center dot
                
            k = cv2.waitKey(1) & 0xFF # Press 'Esc' to exit window
            if k == 27:
                break
        
        # Release everything if job is finished   
        cap.release()
        cv2.destroyAllWindows()
        
############################################################################################
        
        
              

# 3. Track and count objects passing by 
        # OBJECT args = 
        # https://www.analyticsvidhya.com/blog/2022/05/a-tutorial-on-centroid-tracker-counter-system/

