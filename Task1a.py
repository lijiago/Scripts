##---------------------------------------------------------------------
## Task1a.py
##
## Description: Creating the initial buffer script
##
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859)
##---------------------------------------------------------------------

# import system modules
import arcpy

# Set local variables 
in_features = "V:/ENV859_PS4/Data/streams.shp"
out_feature_class = "V:/ENV859_PS4/Scratch/StrmBuff1km.shp"
buffDist = "1000 meters"

# Buffer the results
arcpy.Buffer_analysis(in_features, out_feature_class,buffDist,'FULL','ROUND','ALL')

print(arcpy.GetMessages)

