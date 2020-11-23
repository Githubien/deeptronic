#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from skimage import io

class ImgProcessor:
	def __init__(self,fn):
		self.filename=fn
		img0 = io.imread(self.filename)


def main():
	imp=ImgProcessor(os.path.join("import", 'img_2698.jpg'))
	


if __name__ == "__main__":
	# execute only if run as a script
	main()
