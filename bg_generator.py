import cv2
import numpy as np
import argparse
import sys

def MovingAvg(source, output="bg.png", val=0.01):

	max_frames = source.get(cv2.CAP_PROP_FRAME_COUNT)

	#Read source input
	_,f = source.read()
	if f is None:
		print("No source input")
		return

	#height and width of source
	h, w = f.shape[:2]

	#initializing variables
	avg = np.float32(0.1*f)
	res = avg

	min_density = 1

	first_loop_flag = 1
	frame_count = 1

	while(1):
		_,f = source.read()
		if f is None:
			print("Source input over")
			break

		progress_bar(frame_count, end=max_frames)
		frame_count+=1

		#Calculate moving average
		avg = cv2.accumulateWeighted(f, avg, val)

		res_before = res
		res = cv2.convertScaleAbs(avg)

		#Find least changing moving average and write to output
		if(not first_loop_flag):
			diff_array = cv2.absdiff(res_before, res)
			diff = np.sum(diff_array)
			diff_density = diff/(w*h)

			if(diff_density<min_density):
				min_density = diff_density
				if(show_process):
					cv2.imshow('bg_optimal', res)
				cv2.imwrite(output, res)				


		first_loop_flag = 0

		#Display source and moving average
		if(show_process):
			cv2.imshow('source', f)
			cv2.imshow('moving_average', res)

			#Keystroke check, ESC for exit
			k = cv2.waitKey(1)
			if k & 255 == 27:
				break

	print("Background image at " + output)

	if(show_process):
		cv2.destroyAllWindows()

#creating a progress bar
def progress_bar(val, start=0, end=100, style='percent', fill='='):
	if(val>end):
		val = end
	elif (val<start):
		val = start

	percent = int(val*100/(end-start))
	
	if(style == 'bar'):
		sys.stdout.write("Progress: [")
		for i in range(50):
			if(i<percent/2):
				sys.stdout.write(fill)
			else:
				sys.stdout.write(" ")
		sys.stdout.write("]")

	#Default style is percent
	else:
		sys.stdout.write("Progress: " + str(percent) + "%")
	
	sys.stdout.write("\r")
	


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, 
	help="Filename of input video")
ap.add_argument("-p", "--project", action="store_true", 
	help="Project images as it is processed")
ap.add_argument("-o", "--output", default='bg.png', 
	help="Filename for background image with extension")
ap.add_argument("-val", "--value", default=0.1, 
	help="Value to be used for moving average")
args = ap.parse_args()

source = args.input
show_process = args.project
output = args.output
value = float(args.value)

cam = cv2.VideoCapture(source)

MovingAvg(cam, output=output, val=value)

cam.release()
