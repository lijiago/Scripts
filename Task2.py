##---------------------------------------------------------------------
## Task2.py
##
## Description: Iterating through multi-value string
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
in_features = "Roads.shp"
ROAD_TYPE = "0;201;203"
Road_Type_List = ROAD_TYPE.split(';')


# Buffer the results, iterating through the list
for i in Road_Type_List:
    where_clause = f'"ROAD_TYPE" = {i}'
    out_feature_class = (f"V:/ENV859_PS4/Scratch/roads_{int(i)}.shp")
    arcpy.Select_analysis(in_features, out_feature_class, where_clause)



