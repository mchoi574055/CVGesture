 # Edge Impulse - OpenMV Image Classification Example

import sensor, image, time, os, tf, uos, gc, network, socket

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.
sensor.set_vflip(True)


net = None
labels = None

try:
    # Load built in model
    labels, net = tf.load_builtin_model('trained')
except Exception as e:
    raise Exception(e)


clock = time.clock()
while(True):
    clock.tick()

    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in net.classify(img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
       # print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))

        max_p = predictions_list[0][1]
        max_index = 0
        count = 0
        for i in range(len(predictions_list)):
           # print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))
           if (predictions_list[i][1] > max_p):
                max_index = count
                max_p = predictions_list[i][1]
           count = count + 1

        if (max_p > 0.25):
            print("%s" % (predictions_list[max_index][0]))
            #print(predictions_list[max_index][1])

