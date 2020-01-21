from PIL import Image
pic=Image.new('RGB',(1530,50))
total=-1
r,g,b=255,0,0
def color_line():
   for j in range(50):
      color=(r,g,b)
      address=(total,j)
      pic.putpixel(address,color)
def run(fun):
   global total
   for i in range(1,256):
      total+=1
      fun()
      color_line()
def ramp_red():global r;r+=1
def dec_red():global r;r-=1
def ramp_green():global g;g+=1
def dec_green():global g;g-=1
def ramp_blue():global b;b+=1
def dec_blue():global b;b-=1
run(ramp_green)
run(dec_red)
run(ramp_blue)
run(dec_green)
run(ramp_red)
run(dec_blue)
print(total)
pic.save('rainbow.png')

