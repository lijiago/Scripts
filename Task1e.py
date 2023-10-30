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
buffDist = sys.argv[1]
out_feature_class = (f"V:/ENV859_PS4/Scratch/StrmBuff{int(buffDist)}m.shp")

# Buffer the results
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist,'FULL','ROUND','ALL')

print(arcpy.GetMessages)