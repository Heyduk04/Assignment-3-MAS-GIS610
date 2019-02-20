import arcpy

arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb'

arcpy.env.overwriteOutput = True 

censusTracts = 'Tracts'

generalOff = 'General_Offense' 

arcpy.SpatialJoin_analysis(censusTracts,generalOff,'JOIN_ONE_TO_MANY')