 
import subprocess
import os
os.add_dll_directory('C:/gstreamer/1.0/x86_64/bin')
import cv2

pipeline_description = (
    #"v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=I420 ! "
    "videotestsrc !"
    "x264enc speed-preset=ultrafast tune=zerolatency ! h264parse ! "
    #"rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=5000"
    "rtph264pay config-interval=1 pt=96 ! udpsink host=239.192.3.52 port=37004"
)

# GStreamerパイプラインを作成
pipeline = os.popen("gst-launch-1.0 -e " + pipeline_description, "w")
pipeline.close()
