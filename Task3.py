##---------------------------------------------------------------------
## Task3.py
##
## Description: Split analysis
##
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859)
##---------------------------------------------------------------------

# import system modules
import arcpy
import os
import sys

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True 

# Set local variables 
TriCounties_fc = "V:\\ENV859_PS4\\Data\\TriCounties.shp"

# creating a list of all 5 features that start with "BMR" in its name
point_fc_shp = arcpy.ListFeatureClasses(wild_card = 'BMR*')
#removing .shp in list using .replace function
point_fc = [item.replace('.shp', '') for item in point_fc_shp]

# Checking if product edition is available 
if arcpy.CheckProduct("ArcInfo") == "Available":
    # conducting split analysis for items in list using a for loop
    # saving output to specific folder 
    for i in point_fc:
        inFeatures = i
        splitFeatures = TriCounties_fc
        splitField = "CO_NAME"
        newfolders = arcpy.CreateFolder_management("V:\\ENV859_PS4\\Scratch", f"{i}")
        arcpy.Split_analysis(in_features = inFeatures, split_features = splitFeatures, split_field = splitField, out_workspace = newfolders)
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)


