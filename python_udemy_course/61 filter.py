from PIL import Image, ImageFilter

img = Image.open('merge_two.jpg')

img2 = img.convert("L")
img_blur = img2.filter( ImageFilter.BLUR )

img_detail = img2.filter(ImageFilter.DETAIL)

img_edges = img2.filter(ImageFilter.FIND_EDGES)

img_contour = img2.filter(ImageFilter.CONTOUR)

img_emboss = img2.filter(ImageFilter.EMBOSS)

img_smooth = img2.filter(ImageFilter.SMOOTH)

img_smooth_more = img2.filter(ImageFilter.SMOOTH_MORE)

img_sharp = img2.filter(ImageFilter.SHARPEN)

#img2.show()

#img_blur.show()

#img_detail.show()

#img_edges.show()

#img_contour.show()

#img_emboss.show()

#img_smooth.show()

#img_smooth_more.show()

img_sharp.show()