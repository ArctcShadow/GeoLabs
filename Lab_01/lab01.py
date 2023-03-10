import numpy as np
import rasterio 

data = rasterio.open('soil_moisture.tif')
print("bounds = ", data.count)
print ("CRS = ",data.crs)
print(data.width)
print(data.height)
print(data.bounds)
print(data.transform)