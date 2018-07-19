from PIL import Image

img1=Image.open('image_one.jpg')
img2=Image.open('image_two.jpg')

x,y=img2.size
print(x,y)

img1.paste( img2, (x,y) )
img1.show()
