##---------------------------------------------------------------------
## Task4.py
##
## Description: Script tool to run via ArcGIS pro 
##
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859)
##---------------------------------------------------------------------

import arcpy
import sys
import os

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True 

#Set variable names to user inputs
inFC = arcpy.GetParameterAsText(0)


# Describe a feature class using arcpy.Describe
desc = arcpy.Describe(inFC)

# indicating catalogPath property
if hasattr(desc, "catalogPath"):
   arcpy.AddMessage("CatalogPath: " + desc.catalogPath)
   # reporting the extent of the dataset
   arcpy.AddMessage(("Extent:\nXMin: {0} \nYMin: {1} \nXMax: {2}\nYMax: {3}".format(round(desc.extent.XMin, 1), round(desc.extent.YMin,1), round(desc.extent.XMax,1), round(desc.extent.YMax,1))))
  
  # if statement for FeatureClass that reports dataset's shapeType as a warning message
if desc.datasetType == "FeatureClass":
      arcpy.AddWarning("ShapeType: %s" %desc.shapeType)

# elif statement for RasterDataset that reports dataset's format, rows and columns as warning message
elif desc.datasetType == "RasterDataset":
      arcpy.AddWarning("Raster Format: %s" % desc.format)
      arcpy.AddWarning("# of rows: %s" % desc.height)
      arcpy.AddWarning("# of cols: %s" % desc.width)

# else statement to print out dataset type as error message
else:
      arcpy.AddError("Dataset Type: %s" + desc.datasetType)

