# host.py
# Description: This program retrieves streaming images from the OpenMV camera via USB.
# Author: Michael Fitzgerald (heavily adapted from OpenMV examples)
# (This should be run on a Linux PC, next to the file `rpc.py`!)

import cv2
import io
import numpy as np
import rpc
import serial
from serial.tools import list_ports
import socket
import sys

SERIAL_PATH = "/dev/ttyACM0"

# create RPC serial interface
interface = rpc.rpc_usb_vcp_master(port=SERIAL_PATH)

# define callback for OpenCV
# this decodes the JPEG data, then upscales and outputs it
def img_callback(data):
    img_encoded = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(img_encoded, -1)
    img = cv2.resize(img, dsize=None, fx=2, fy=2)
    cv2.imshow("OpenMV Streaming to OpenCV", img)
    if cv2.waitKey(33) == 27:
        print("Ended normally.")
        exit()

# loop to get image
try:
    while(True):
        res = interface.call("jpeg_image_stream", "sensor.RGB565,sensor.QQVGA")
        if res is not None:
            # start streaming on success
            interface.stream_reader(img_callback, queue_depth=8)

    
except KeyboardInterrupt:
    print("Ended normally.")