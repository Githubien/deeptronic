#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from skimage import io
from skimage import color
from skimage import transform
from skimage import feature

import matplotlib.pyplot as plt
from matplotlib import cm

class ImgProcessor:
	def __init__(self,fn,debug=0):
		self.filename=fn
		self.debug=debug

	def Process(self):
		img0 = io.imread(self.filename)
		img1 = color.rgb2gray(img0)
		if (self.debug): self.Display(img0,img1)
		img2 = transform.rescale(img1, 0.25, anti_aliasing=True)
		if (self.debug): self.Display(img1,img2)
		img3 = feature.canny(img2)
		if (self.debug): self.Display(img2,img3)
	
	def Display(self,imga,imgb):
		fig, axes = plt.subplots(1, 2, figsize=(15, 6))
		ax = axes.ravel()
		ax[0].imshow(imga, cmap=cm.gray)
		ax[0].set_title('Step n')
		ax[0].set_axis_off()
		ax[1].imshow(imgb, cmap=cm.gray)
		ax[1].set_title('Step n+1')
		ax[1].set_axis_off()
		
		plt.tight_layout()
		plt.show()



def main():
	imp=ImgProcessor(os.path.join("import", 'img_2698.jpg'),1)
	imp.Process()
	


if __name__ == "__main__":
	# execute only if run as a script
	main()
