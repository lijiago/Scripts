##---------------------------------------------------------------------
## Task1c.py
##
## Description: Enabling user input
##
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859)
##---------------------------------------------------------------------

# import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True 

# Set local variables 
in_features = "streams.shp"
out_feature_class = sys.argv[2]
buffDist = sys.argv[1]

# Buffer the results
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist,'FULL','ROUND','ALL')

print(arcpy.GetMessages)