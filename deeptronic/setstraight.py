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

	def process(self):
		self.extract_lines()
		self.fit_lines()
		
		
	def extract_lines(self):
		img0 = io.imread(self.filename)
		img1 = color.rgb2gray(img0)
		#if (self.debug): self.display(img0,img1)
		img2 = transform.rescale(img1, 0.25, anti_aliasing=True)
		#if (self.debug): self.display(img1,img2)
		img3 = feature.canny(img2)
		#if (self.debug): self.display(img2,img3)

		self.lines = transform.probabilistic_hough_line(img3, threshold=10, line_length=50,
											  line_gap=3)
		if (self.debug): self.display_lines(img3)
	
	def fit_lines(self):
		# FIXME
		return
		
		
	
	def display(self,imga,imgb):
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
		
	def display_lines(self,img):
		fig, axes = plt.subplots(1, 2, figsize=(15, 6))
		ax = axes.ravel()
		ax[0].imshow(img, cmap=cm.gray)
		ax[0].set_title('Step n')
		ax[0].set_axis_off()
		
		ax[1].imshow(img *0)
		for line in self.lines:
			p0, p1 = line
			ax[1].plot((p0[0], p1[0]), (p0[1], p1[1]))
		ax[1].set_xlim((0, img.shape[1]))
		ax[1].set_ylim((img.shape[0], 0))
		ax[1].set_title('Probabilistic Hough')
		
		plt.tight_layout()
		plt.show()

	


def main():
	imp=ImgProcessor(os.path.join("import", 'img_2698.jpg'),1)
	imp.process()
	


if __name__ == "__main__":
	# execute only if run as a script
	main()
