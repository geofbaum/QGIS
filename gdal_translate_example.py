from osgeo import gdal, ogr
from PyQt5.QtGui import *

qid = QInputDialog()

# Create a list of the visible layers present in the project
layers = iface.mapCanvas().layers()

indx = -1

for layer in layers:
    indx = indx + 1
	# Print out to console only Raster layers and their info
    if layer.type() == QgsMapLayer.RasterLayer:
        print("Layer: ",layer)
        print("Name: ",layer.name())
        print("ID: ",layer.id())
        print("Index Number: ",indx)
        #layerIDs.append(layer.id())
        print("---------")

# Set parameters for User Input Dialog window
title = "Enter the index number for the file you want to choose"
label = "Index: "
mode = QLineEdit.Normal
default = "<your index number here>"

# User Input dialog window
index_value, ok = QInputDialog.getText(qid, title, label, mode, default)

# Using user input get correct layer to put into gdal.Translate()
# Then get path for that layer file
# Finally set output file path
rLayer = layers[int(index_value)]
input_layer = str(rLayer.source())
output_rLayer = "C:/Path/To/Output_file/translate_out_test.tif"

gdal.Translate(output_rLayer, input_layer, format="GTiff")
# Normally I wouldn't worry about any or most of the options since I'd
# send this file directly to gdal.Warp() where I could set a lot of the same
# options. One option however that would probably be used in that situation
# is the one for GCPs. In the file for the georeferencer example that option
# will be shown. For this example I'm only setting the output format.


# Add output from gdal.Translate() to the canvas.
iface.addRasterLayer(output_rLayer, 'translate_out_test')

# End of Code

#
#
#
# List of Keyword arguments that can be used with gdal.Translate()
# Please see https://gdal.org/python/osgeo.gdal-module.html#TranslateOptions
#
# Keyword arguments are :
#  options --- can be be an array of strings, a string or let empty and filled from other keywords.
#  format --- output format ("GTiff", etc...)
#  outputType --- output type (gdal.GDT_Byte, etc...)
#  bandList --- array of band numbers (index start at 1)
#  maskBand --- mask band to generate or not ("none", "auto", "mask", 1, ...)
#  width --- width of the output raster in pixel
#  height --- height of the output raster in pixel
#  widthPct --- width of the output raster in percentage (100 = original width)
#  heightPct --- height of the output raster in percentage (100 = original height)
#  xRes --- output horizontal resolution
#  yRes --- output vertical resolution
#  creationOptions --- list of creation options
#  srcWin --- subwindow in pixels to extract: [left_x, top_y, width, height]
#  projWin --- subwindow in projected coordinates to extract: [ulx, uly, lrx, lry]
#  projWinSRS --- SRS in which projWin is expressed
#  strict --- strict mode
#  unscale --- unscale values with scale and offset metadata
#  scaleParams --- list of scale parameters, each of the form [src_min,src_max] or [src_min,src_max,dst_min,dst_max]
#  exponents --- list of exponentiation parameters
#  outputBounds --- assigned output bounds: [ulx, uly, lrx, lry]
#  metadataOptions --- list of metadata options
#  outputSRS --- assigned output SRS
#  GCPs --- list of GCPs
#  noData --- nodata value (or "none" to unset it)
#  rgbExpand --- Color palette expansion mode: "gray", "rgb", "rgba"
#  stats --- whether to calculate statistics
#  rat --- whether to write source RAT
#  resampleAlg --- resampling mode
#  callback --- callback method
#  callback_data --- user data for callback
