import arcpy

from arcpy import env

env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb'

lyrfile = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\CallsforService'

result = arcpy.GetCount_management(lyrfile)

count = int(result.getOutput(0))

print(count)
