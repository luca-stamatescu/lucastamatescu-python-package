# lucastamatescu-python-package

## Logo overlay 

Instanstiate the class, passing in the file as a argument, and the name of the window used in the imshow function later in the script
> objectvideo = overlay.video_overlay_class('logo.png','video_output')

Within the video processing loop, use the below line to add the overlay:
> frame = objectvideo.overlay_image(frame)

## RTSP Streaming

See the "rtspstreaming_example.py" file located in the "examples" directory.

Explanation of the relevant code:

Import the relevant functionality:
>from lucastamatescu import rtspstreaming

Start the RTSP streaming thread.
>frame_queue=rtspstreaming.start_rtsp_streaming()

In the loop performing the computer vision processing, update the frame each loop. The RTSP stream loops and continuously streams the most recent frame.
>rtspstreaming.update_frame(frame_queue, frame)

In another terminal, use the following command to receive the RTSP stream using Gstreamer. Any other relevant RTSP streaming tool can be used to view the video.
>gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/test latency=50 ! decodebin ! autovideosink

Port forwarding can be used to expose the RTSP to the internet- replace locahost with your public IP.

### Dependencies

This application requires Gstream to be installed.
The "gi" module was also required- this is installed using 
>pip install gi

On Mac, installing "pyGObject" was required also.
>pip install pygobject

The following packages should also be installed with Brew on Mac, or the equivalent on Linux.
gst-libav
gst-plugins-base
gst-plugins-good
gst-plugins-ugly
gst-rtsp-server
gstreamer

## Commands to create package:

python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*



