#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  imagediff.py
#  
#  Copyright 2016 Franz Habison <habison.franz@gmx.at>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#Quelle: http://www.blog.pythonlibrary.org/2016/10/11/how-to-create-a-diff-of-an-image-in-python/

import Image
import ImageChops

def compare_images(path_one, path_two, diff_save_location):
    """
    Compares to images and saves a diff image, if there
    is a difference
 
    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    print "Test"
    diff = ImageChops.difference(image_one, image_two)
 
    if diff.getbbox():
        print "Test2"
        diff.save(diff_save_location)
 
 
if __name__ == '__main__':
    compare_images('/home/franz/Downloads/Bilder/image1.jpg',
                   '/home/franz/Downloads/Bilder/image2.jpg',
                   '/home/franz/Downloads/Bilder/diff.jpg')

