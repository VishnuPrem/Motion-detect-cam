# Motion-detect-cam
A webcam captures images and this feed is sent to a computer. The images are processed using Python with OpenCV. This is done by subtracting the consecutive images with the next image obtained from the camera feed. The resulting image will show just the regions in motion. This resulting image is divided into three regions: left, middle and right. The region with the most movement is where the camera is required to point.
 After the direction of motion is detected it is sent to another python program through a file which sends this data to the Arduino via serial communication.
The Arduino controls a servo motor which is placed on the bottom of the webcam. Hence, the camera turns in the direction of the detected motion.

motion follow.py contains the python code which detect the motion and it position and sends this information to a .txt file

serial comm.py fetches this information and sends it to the arduino via serial communication

new.txt is the text file used for this purpose

arduinocode.ino contains the code which reads the serially communicated data from the python program and controls the servo accordingly
