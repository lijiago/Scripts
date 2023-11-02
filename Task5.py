##---------------------------------------------------------------------
## Task5.py
##
## Description: Script tool
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

#Set variable names to the 2 user inputs
inFC = arcpy.GetParameterAsText(0)
field = arcpy.GetParameterAsText(1) #this has to be field from that feature class

# Creating the point object
myPoint = arcpy.Point(X=621000,Y=254000)
# Creating searchcursor the retrieve Shape and the field user specifies 
rows = arcpy.da.SearchCursor(inFC,['Shape@', f"{field}"])

# For loop to determine if point created in falls within recShape
for row in rows: 
    recShape = row[0]
    if recShape.contains(myPoint):
        field_value = row[1]

        arcpy.AddMessage(f"The field's value is {field_value}")


