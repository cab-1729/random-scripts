from random import randrange,choice
from argparse import ArgumentParser
from itertools import product
from PIL import Image
interface=ArgumentParser(description="Polygon artwork")
interface.add_argument('--colors',type=str,required=False,default='''(
	(255,51,0),#red
	(255,153,51),#orange
	(255,255,0),#yellow
	(52,204,51),#green
	(0,51,204),#blue
	(0,204,255),#cyan
	(255,51,204),#pink
	(153,0,204),#violet
)''',help='RGB colors to be used')
interface.add_argument('--density',type=int,required=False,default=10,help='density of colors')
interface.add_argument('--dimensions',type=str,required=False,default='800x800',help='dimensions of the image')
interface.add_argument('--save',type=str,required=False,help='where to save the image')
args=interface.parse_args()
bright_colors=eval(args.colors)
x1=args.dimensions.index('x')
side_x=int(args.dimensions[:x1])
side_y=int(args.dimensions[x1+1:])
art=Image.new('RGB',(side_x,side_y))
segments=[product(range(side_x),range(side_y))]
for line in range(randrange(args.density,args.density+21)):#number of lines
	new_segments=[]
	x1,y1,x2,y2=randrange(side_x),randrange(side_y),randrange(side_x),randrange(side_y)
	try:
		slope=(y2-y1)/(x2-x1)
		one_side=lambda x,y:(x-x1)*slope-y+y1>0
	except ZeroDivisionError:
		one_side=lambda x,y:x>x1
	for segment in segments:
		side1=[];side2=[]
		for px,py in segment:
			if one_side(px,py):side1.append((px,py))
			else:side2.append((px,py))
		if side1!=[]:new_segments.append(side1)
		if side2!=[]:new_segments.append(side2)
	segments=new_segments.copy()
for segment in segments:
	color=choice(bright_colors)
	for point in segment:
		art.putpixel(point,color)
if args.save==None:art.show()
else:art.save(args.save)
