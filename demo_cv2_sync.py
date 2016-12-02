
import freenect
import cv2
import frame_convert2

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth())


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video())


while 1:
    cv2.imshow('Depth', get_depth())
    cv2.imshow('Video', get_video())
    cv2.imwrite('Video.jpg',get_depth())
    if cv2.waitKey(10) == 27:
        break
