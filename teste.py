import freenect
import cv2
import numpy as np
import owncloud
import time

i = 0
cascade_src = 'cars.xml'

#oc = owncloud.Client('http://nuvem.cct.uema.br')
#oc.login('urca', 'KvZC-T5pe-8HmP')
#oc.mkdir('URCA')
#oc.mkdir('URCA/DEPTH')
#oc.mkdir('URCA/RGB')


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

#        cv2.imwrite('../URCA/DEPTH/Depth image' + str(i) + '.jpg', depth)
#       cv2.imwrite('../URCA/RGB/RGB image' + str(i) + '.jpg', frame)
        i = i + 1

#      oc.put_directory('URCA/', 'URCA/')
#       time.sleep(120)
        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
