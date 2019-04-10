from osgeo import gdal, ogr
from PyQt5.QtGui import *

qid = QInputDialog()

# grabs only the visible layers that are in Layers tab
layers = iface.mapCanvas().layers()

indx = -1

for layer in layers:
    indx = indx + 1
    # For this example I only want to grab Raster layers
    # Prints out the layer, the layers name, id, and the 
    #index position within the layers group
    if layer.type() == QgsMapLayer.RasterLayer:
        print("Layer: ",layer)
        print("Name: ",layer.name())
        print("ID: ",layer.id())
        print(indx)
        print("---------")

# Next we'll setup the Input Dialog info: window title, 
# input box label, mode, and default value for input box
title = "Enter the index number for the file you want to choose"
label = "Index: "
mode = QLineEdit.Normal
default = "<your index number here>"

# Get User Input for the appropriate index value corresponding
# to the raster layer you want to input into gdal.Warp()
index_value, ok = QInputDialog.getText(qid, title, label, mode, default)

# Set user response as an integer so we can grab the appropriate layer with its index
# Then set the path to the raster layer file as a string
# Finally output file path, remember to input your correct destination
rLayer = layers[int(index_value)]
input_layer = str(rLayer.source())
output_rLayer = "C:/Path/To/File/out_test.tif"

# gdal.Warp() needs two mandatory pieces of info (input and output file paths) 
# plus any keywords (see below for a list of all of them).
# In the line below you can see I'm setting the resolution of each pixel in the
# current CRS format (here it's in meters), then the format of the output 
# file (GTiff), and the resampling algorthim I'm using (Bilinear).
# There are plenty of other keywords available to set as well. If you have to 
# do this for a lot of files, and would use the same settings for each it might
# be simpler to use gdal.WarpOptions() and reference that in your gdal.Warp() 
# call instead of having a long list of keyword arguements.

gdal.Warp(output_rLayer, input_rLayer, xRes=0.5, yRes=0.5, format="GTiff", resampleAlg="Bilinear")

# Add warped layer to your QGIS project (file_path, file_name_to_be_used)
iface.addRasterLayer(output_rLayer, 'out_test')  

# End of Code


#
#
#
# Other gdal.Warp() options are shared below:
# Please see https://www.gdal.org/gdalwarp.html and https://gdal.org/python/osgeo.gdal-pysrc.html#Warp for more info
# Keyword arguments are : 
# options --- can be be an array of strings, a string or let empty and filled from other keywords. 
# format --- output format ("GTiff", etc...) 
# outputBounds --- output bounds as (minX, minY, maxX, maxY) in target SRS 
# outputBoundsSRS --- SRS in which output bounds are expressed, in the case they are not expressed in dstSRS 
# xRes, yRes --- output resolution in target SRS 
# targetAlignedPixels --- whether to force output bounds to be multiple of output resolution 
# width --- width of the output raster in pixel 
# height --- height of the output raster in pixel 
# srcSRS --- source SRS 
# dstSRS --- output SRS 
# srcAlpha --- whether to force the last band of the input dataset to be considered as an alpha band 
# dstAlpha --- whether to force the creation of an output alpha band 
# outputType --- output type (gdal.GDT_Byte, etc...) 
# workingType --- working type (gdal.GDT_Byte, etc...) 
# warpOptions --- list of warping options 
# errorThreshold --- error threshold for approximation transformer (in pixels) 
# warpMemoryLimit --- size of working buffer in bytes 
# resampleAlg --- resampling mode --- choices are Near, Bilinear, Cubic, Cubicspline, Lanczos, Average, Mode, Max, Min, Med, q1, q3
# creationOptions --- list of creation options 
# srcNodata --- source nodata value(s) 
# dstNodata --- output nodata value(s) 
# multithread --- whether to multithread computation and I/O operations 
# tps --- whether to use Thin Plate Spline GCP transformer 
# rpc --- whether to use RPC transformer 
# geoloc --- whether to use GeoLocation array transformer 
# polynomialOrder --- order of polynomial GCP interpolation 
# transformerOptions --- list of transformer options 
# cutlineDSName --- cutline dataset name 
# cutlineLayer --- cutline layer name 
# cutlineWhere --- cutline WHERE clause 
# cutlineSQL --- cutline SQL statement 
# cutlineBlend --- cutline blend distance in pixels 
# cropToCutline --- whether to use cutline extent for output bounds 
# copyMetadata --- whether to copy source metadata 
# metadataConflictValue --- metadata data conflict value 
# setColorInterpretation --- whether to force color interpretation of input bands to output bands 
# callback --- callback method 
# callback_data --- user data for callback 
