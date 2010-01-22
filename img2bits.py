#!/opt/local/bin/python2.5

import Image, sys, os.path, shutil
 
args = sys.argv
 
src = args[1]
 

if len(args) == 4 or len(args) == 5:
	left = int(args[2])
	right = int(args[3])
if len(args) == 6 or len(args) == 7:
	left = int(args[2])
	top = int(args[3])
	right = int(args[4])
	bottom = int(args[5])

if len(args) == 5 or len(args) == 7:
	result_dir = args[-1]

if not result_dir:
	result_dir = os.path.dirname(src) if os.path.isabs(src) else os.path.join('.', os.path.dirname(src))

img_name, img_type = os.path.basename(src).split('.')

 
if len(args) == 6 or len(args) == 7:
	coords = (left, top, right, bottom)
else:
	coords = (left, right)
 
im = Image.open(src)
 
if 'transparency' in im.info:
	transparency = im.info['transparency']
else:
	transparency = 0
 
width, height = im.size
 
if len(args) == 6 or len(args) == 7:
	boxes = {
	  "tl": (0, 0, coords[0], coords[1]),
	  "tr": (width - coords[2], 0, width, coords[1]),
	  "bl": (0, height - coords[3], coords[0], height),
	  "br": (width - coords[2], height - coords[3], width, height),
	  "t": (coords[0], 0, width - coords[2], coords[1]),
	  "b": (coords[0], height - coords[3], width-coords[2], height),
	  "l": (0, coords[1], coords[0], height - coords[3]),
	  "r": (width - coords[2], coords[1], width, height - coords[3]),
	  "c": (coords[0], coords[1], width - coords[2], height - coords[3])
	}
else:
	boxes = {
	  "l": (0, 0, coords[0], height),
	  "r": (width - coords[1], 0, width, height),
	  "c": (coords[0], 0, width - coords[1], height)
	}

for box in boxes:
	im.crop(boxes[box]).save(result_dir + '/' + img_name + '-' + box + '.' + img_type)
 
