# This question took me the longest to complete and I still couldn't get it to run correclty. The examples on 
# http://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm were not helpful either.

import arcpy 
arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb'
arcpy.env.overwriteOutput = True
SelectFc = (r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\General_Offense')
fieldFc = 'OffenseCustom'
AddFc = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\CallsforService'
arcpy.MakeFeatureLayer_management('SelectFc','General_OffenseLayer_lyr')
arcpy.SelectLayerByAttribute_management('General_OffenseLayer_lyr','NewLayer', 'x_rand > 10')
arcpy.CopyFeatures_management('General_OffenseLayer_lyr',r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\NewLayer')