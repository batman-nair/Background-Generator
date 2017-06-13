# Background-Generator  

### Background Generator script using Python 2.7 and OpenCV 3.1


The script can be used in command line to generate the background for a video input

```
usage: bg_generator.py [-h] -i INPUT [-p] [-o OUTPUT] [-val VALUE]

Generate background for video input

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of input video (default: None)
  -p, --project         Project images as it is processed (default: False)
  -o OUTPUT, --output OUTPUT
                        Filename for background image with extension (default:
                        bg.png)
  -val VALUE, --value VALUE
                        Value to be used for moving average (default: 0.1)

```

Example : ` python bg_generator.py -i sample/video.mp4 -o sample/bg.png `


Try with `-v 0.01` for more finer background generation


[Sample Video source](https://www.youtube.com/watch?v=GGxQDT4c5TY)