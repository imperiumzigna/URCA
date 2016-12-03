# Written by Igor Amorim Silva ~ 2016
# Version: 1.0.0
# -*- coding: utf-8 -*-
from gpiozero import MotionSensor
from datetime import datetime
import freenect
import cv2
import numpy as np
import owncloud

# General paths where to save data
urca_path = 'URCA'
depth_path = 'URCA/DEPTH/'
rgb_path = 'URCA/RGB/'
# Start the PIR sensor on GPIO - 4
sensor = MotionSensor(4)
# Get the current date of today
today = str(datetime.date.today())
i = 0
# Conection with owncloud server
oc = owncloud.Client('http://nuvem.cct.uema.br')
oc.login('urca', 'KvZC-T5pe-8HmP')
oc.mkdir(urca_path)

oc.mkdir(depth_path + today)
oc.mkdir(rgb_path + today)

# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    
    return array


if __name__ == "__main__":
    while 1:

        # get a frame from RGB camera
        frame = get_video()
        # get a frame from depth sensor
        depth = get_depth()
        # display RGB image
        cv2.imshow('RGB image', frame)
        # display depth image
        cv2.imshow('Depth image', depth)

        # If a person is detected print image on file and send to cloud
        if sensor.motion_detected:
            time_now = str(datetime.now())
            cv2.imwrite('../URCA/DEPTH/' + today + '/' + time_now + '.jpg', depth)
            cv2.imwrite('../URCA/RGB/' + today + '/' + time_now + '.jpg', frame)
            oc.put_directory('URCA/', 'URCA/')

        # Test current date for file management issues
        if today == str(datetime.date.today()):
            today = str(datetime.date.today())
            oc.mkdir(depth_path + today)
            oc.mkdir(rgb_path + today)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
