from osgeo import gdal
from PyQt5.QtGui import *

qid = QInputDialog()

layers = iface.mapCanvas().layers()

# gdal.GCPs are in the following format: gdal.GCP(x, y, z, col/pixel, row/line)
# https://gdal.org/python/osgeo.gdal-pysrc.html#GCP.__init__

# Hardcoded in this example for simplicity and to show an example.
# File that I used for creating this example is in EPSG:32618 (WGS 84/UTM Zone 18N)

# I chose to use three GCPs since while not necessary for all of the resampling techniques, it is necessary for some types.
gcp = [gdal.GCP(608219.1, 5000622.62, 51),gdal.GCP(608731.42, 5000712.73, 51),gdal.GCP(608420.77, 5000422.68, 52)] 

indx = -1

for layer in layers:
	indx = indx + 1
	if layer.type() == QgsMapLayer.RasterLayer:
		print("Layer: ",layer)
		print("Name: ",layer.name())
		print("ID: ",layer.id())
		print("Index Number: ",indx)
		#layerIDs.append(layer.id())
		print("---------")


title = "Enter the index number for the file you want to choose"
label = "Index: "
mode = QLineEdit.Normal
default = "<your index number here>"

index_value, ok = QInputDialog.getText(qid, title, label, mode, default)

rLayer = layers[int(index_value)]
input_layer = str(rLayer.source())
fname = str(layers[int(index_value)].name())+".tif"
print(fname)
temp_output = "C:/Path/To/Temp/Folder/"+fname

ex = rLayer.extent()
xmax = ex.xMaximum()
ymax = ex.yMaximum()
xmin = ex.xMinimum()
ymin = ex.yMinimum()

exten = [xmin, ymax, xmax, ymin]  # format: [ulx, uly, lrx, lry]

gdal.translate(temp_output, input_layer, outputBounds=exten, outputSRS="EPSG:32618", format="GTiff", GCPs=gcp)

georef_out = "C:/Path/To/Output/Folder/"+fname

gdal.Warp(georef_out, temp_output, format="GTiff", xRes=0.5, yRes=0.5, resampleAlg="Bilinear") # Please see the other options for

iface.addRasterLayer(georef_out, 'georef_out_test')
