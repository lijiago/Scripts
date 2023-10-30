##---------------------------------------------------------------------
## Task1e.py
##
## Description: Iterating through buffer distances 
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
buffDist = ["100", "200", "300", "400", "500"]


# Buffer the results, iterating through the list
for Dist in buffDist:
    out_feature_class = (f"V:/ENV859_PS4/Scratch/StrmBuff{int(Dist)}m.shp")
    arcpy.Buffer_analysis(in_features, out_feature_class, Dist,'FULL','ROUND','ALL')


