# ====================================================================================
# Image filtering functions, tested on a FITS image taken from SkyView 
# Used in the Astrophysical Machine Learning course at the University of Iowa
# https://astrophysicalmachinelearning.wordpress.com/ taught by Shea Brown
# Written by Shea Brown, shea-brown@uiowa.edu, https://sheabrownastro.wordpress.com/
# =====================================================================================
import numpy as np
from astropy.io import fits as fits
import matplotlib.pyplot as plt

image = fits.open('coma_DSSred.fits')
image = np.flipud(image[0].data)

print(image.shape)

filt = (7, 7)
print(filt[0] / 2)
kernel = np.random.normal(size=filt)
maxa = np.zeros((300, 300))
mina = np.zeros((300, 300))
conv_array = np.zeros((300, 300))


def maxFilter(im, s):
    xpix, ypix = im.shape
    maxa = np.zeros(im.shape)
    for i in range(s[0] / 2, xpix - s[0] / 2):
        for j in range(s[1] / 2, ypix - s[1] / 2):
            maxa[i, j] = np.max(im[i - s[0] / 2:i + 1 + s[0] / 2, j - s[1] / 2:j + 1 + s[1] / 2])

    return maxa


def minFilter(im, s):
    xpix, ypix = im.shape
    mina = np.zeros(im.shape)
    for i in range(s[0] / 2, xpix - s[0] / 2):
        for j in range(s[1] / 2, ypix - s[1] / 2):
            mina[i, j] = np.min(im[i - s[0] / 2:i + 1 + s[0] / 2, j - s[1] / 2:j + 1 + s[1] / 2])

    return mina


def medianFilter(im, s):
    xpix, ypix = im.shape
    meda = np.zeros(im.shape)
    for i in range(s[0] / 2, xpix - s[0] / 2):
        for j in range(s[1] / 2, ypix - s[1] / 2):
            meda[i, j] = np.median(im[i - s[0] / 2:i + 1 + s[0] / 2, j - s[1] / 2:j + 1 + s[1] / 2])

    return meda


def meanFilter(im, s):
    xpix, ypix = im.shape
    meana = np.zeros(im.shape)
    for i in range(s[0] / 2, xpix - s[0] / 2):
        for j in range(s[1] / 2, ypix - s[1] / 2):
            meana[i, j] = np.mean(im[i - s[0] / 2:i + 1 + s[0] / 2, j - s[1] / 2:j + 1 + s[1] / 2])

    return meana


maxim = maxFilter(image, filt)
minim = minFilter(image, filt)
open = maxFilter(minim, filt)
medim = medianFilter(image, filt)
meanim = meanFilter(image, filt)
plt.imshow(image - open)
plt.show()
