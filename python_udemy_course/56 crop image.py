from PIL import Image

#this doesn't work. Pretty unclear lecture
img=Image.open('image_one.jpg')

area=(200,200,700,700)

crop_img=img.crop( area )
crop_img.show()
img.show()