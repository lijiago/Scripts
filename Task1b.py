##---------------------------------------------------------------------
## Task1b.py
##
## Description: Setting environment values in script
##
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859)
##---------------------------------------------------------------------

# import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/lg297_PS4/Data"
arcpy.env.overwriteOutput = True 

# Set local variables 
in_features = "streams.shp"
out_feature_class = "V:/lg297_PS4/Scratch/StrmBuff1km.shp"
buffDist = "1000 meters"

# Buffer the results
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist,'FULL','ROUND','ALL')

print(arcpy.GetMessages)