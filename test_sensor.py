from gpiozero import MotionSensor
sensor = MotionSensor(4)

while 1:
    if sensor.motion_detected:
        print 'funciona'
    else:
        print 'nao detectado'
