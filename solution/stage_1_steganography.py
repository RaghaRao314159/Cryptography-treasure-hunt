#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:50:17 2022

@author: Ragha
"""

from PIL import Image 
from numpy import asarray 
import random
import numpy as np
import copy
'=========================================================='
#ENCRYPTION

#Open image
hidden1 = Image.open("image1.png")


#Convert image to array
hidden = asarray(hidden1)


#close image to prevent permeant change before carrying on
hidden1.close()


#do something to array

#print(hidden)

#19 characters
msg = "Initial:a_4,Final:a_18"


#Every character would be converted into their ascii values
def ConvertToAsc(string):
  dic = {}
  for char in string:
    dic[char] = ord(char)
  return dic
  
ascii_dic = ConvertToAsc(msg)
#print(ascii_dic)






def GetAscii(char):
  return ascii_dic[char]
  
  

  
#Generates n numbers from bound range
def GenerateRandom(n, bound):
  random.seed(10)
  lst, counter = [], 0
  while counter != n:
    ran = random.randint(0,bound+1)
    if ran not in lst:
      lst.append(ran)
      counter += 1
  return sorted(lst)

#The random indexes will be used to find random pixel RGBs
random_indexes = GenerateRandom(len(msg), len(hidden))

#Random indexes looks like this
#[60, 133, 140, 182, 311, 568, 656, 844, 1023, 1136, 1342, 1479, 1721, 1756, 1894, 1976, 2007, 2012, 2132, 2340, 2367, 2470]


#ascii_dic looks like this, 22 length
#ascii_dic = {73: 'I', 110: 'n', 105: 'i', 116: 't', 97: 'a', 108: 'l', 58: ':', 95: '_', 52: '4', 44: ',', 70: 'F', 49: '1', 56: '8'}

encrypted = copy.deepcopy(hidden)



def GetPixel(image,r1,r2):
  return image[r1][r2]  


def same_array(array1,array2):
  if array1.shape != array2.shape:
    return False
  else:
    for idx, x in np.ndenumerate(array1):
        if x != array2[idx]:
            return False
    return True
  
#value is the ascii value of character
def EditRGB(pixel,rgb_index,value):
  rgb = pixel[rgb_index]
  total = rgb + value
  if total > 255:
    total = rgb - value
  pixel[rgb_index] = total
  return "Value changed from "+str(rgb)+" to "+str(total)



random.seed(8)
for i in range(len(random_indexes)):
  index = random_indexes[i]
  randpixel = GetPixel(encrypted,index,index)
  randrgb_index = random.randint(0,2)
  EditRGB(randpixel,randrgb_index,GetAscii(msg[i]))

""" change array to image and save (save as png. Saving as jpg causes RBG values to change)"""

encrypted1 = Image.fromarray(encrypted)
encrypted1.save("image0.png")




'=========================================================='
#DECRYPTION

text = ''

for idx, i in np.ndenumerate(encrypted):
  if hidden[idx] != i:
    if i> hidden[idx]:
      text+=chr(i-hidden[idx])
    else: 
      text+= chr(hidden[idx]-i)



print(text)











