# device.py
# Description: This program runs on the OpenMV device and sends JPEG image data to the host machine.
# Author: Michael Fitzgerald (heavily adapted from OpenMV examples)
# (This goes to OpenMV storage root, and should be named `main.py`!)

import network
import omv
import rpc
import sensor

# configure camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# disable IDE frame buffer (since we're not using the IDE)
omv.disable_fb(True)

# create USB interface
interface = rpc.rpc_usb_vcp_slave()

def stream_cb():
    return sensor.snapshot().compress(quality=90).bytearray()

def jpeg_stream_cb():
    interface.stream_writer(stream_cb)

# schedule callback for given image data
def jpeg_image_stream(data):
    # Q: why do we need this part?
    pixformat, framesize = bytes(data).decode().split(",")
    sensor.set_pixformat(eval(pixformat))
    sensor.set_framesize(eval(framesize))
    interface.schedule_callback(jpeg_stream_cb)
    return bytes()

# register callback
interface.register_callback(jpeg_image_stream)

interface.loop()