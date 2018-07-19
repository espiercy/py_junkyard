from PIL import Image

img1 = Image.open('merge_one.jpg')
img2 = Image.open('merge_two.jpg')

r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()
#ok let's get two images of the same size...
img3=Image.merge('RGB', (b1,g2,r2))
img3.show()