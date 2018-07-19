from PIL import Image

img = Image.open('merge_one.jpg');

resize_img=img.resize((500,500))

transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
transpose_img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
transpose_img3 = img.transpose(Image.ROTATE_90)
transpose_img4 = img.transpose(Image.ROTATE_180)
transpose_img5 = img.transpose(Image.ROTATE_270)

#resize_img.show()
#transpose_img.show()
#transpose_img2.show()
#transpose_img3.show()
#transpose_img4.show()
transpose_img5.show()