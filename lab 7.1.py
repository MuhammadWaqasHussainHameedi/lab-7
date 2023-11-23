from astropy.io import fits
import matplotlib.pyplot as plt

# Open a FITS file
hdulist = fits.open('E:\DS9_Practice_images\M5\m5 dss2 nir.fits') #nir  is green color

# Access the data in the primary HDU (Header Data Unit)
data = hdulist[0].data
hdulist.close()
plt.imshow(data, cmap='gray')
plt.show()
header = hdulist[0].header
print(header)