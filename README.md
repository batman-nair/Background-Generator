# Background-Generator
###Background Generator script using Python 2.7 and OpenCV 3.1


The script can be used in command line to generate the background for a video input

```
usage: bg_generator.py [-h] -i INPUT [-p] [-o OUTPUT] [-val VALUE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of input video
  -p, --project         Project images as it is processed
  -o OUTPUT, --output OUTPUT
                        Filename for background image with extension
  -val VALUE, --value VALUE
                        Value to be used for moving average

```

Example : ` python bg_generator.py -i sample/video.mp4 -o sample/bg.png `


Sample Video source : https://www.youtube.com/watch?v=GGxQDT4c5TY