# Imports
from ultralytics import YOLOWorld
# import RPi.GPIO as GPIO
from cv2 import VideoCapture
import ssl

# # Output pwm for servo
# # def pwmOut(px: float):
# #     x = abs(640 - px)

# # Move based on pwm
# def servoShift():
#     dx = abs(640 - )

# # GPIO
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT) # servo motor
# GPIO.setup(21, GPIO.OUT) # laser

# pwm = GPIO.PWM(21, 50)

# webcam = VideoCapture(0)

# Target tracking
ssl._create_default_https_context = ssl._create_unverified_context
model = YOLOWorld("yolov8s-worldv2.pt")
model.set_classes(["person"])
predict = model.predict("image.jpg")
print(predict[0].boxes.xyxy)