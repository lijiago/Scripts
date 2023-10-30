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

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True 

# Set local variables 
TriCounties_fc = "V:\\ENV859_PS4\\Data\\TriCounties.shp"

# creating a list of all 5 features that start with "BMR" in its name
point_fc = arcpy.ListFeatureClasses(wild_card = 'BMR*')

# Checking if product edition
if arcpy.CheckProduct("ArcInfo") == "Available":
    for i in point_fc:
        inFeatures = i
        splitFeatures = TriCounties_fc
        splitField = "CO_NAME"
        newfolders = arcpy.CreateFolder_management("V:\\ENV859_PS4\\Scratch", f'{i}')
        folderlist = newfolders
        arcpy.Split_analysis(in_features = inFeatures, split_features = splitFeatures, split_field = splitField, out_workspace = newfolders[i])
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)

data_folder = r'W:\859_data\triangle'

data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

user_item = "roads.shp"

data_list.append(user_item)

for N in data_list: 
    print(data_folder  + "\\" + N)