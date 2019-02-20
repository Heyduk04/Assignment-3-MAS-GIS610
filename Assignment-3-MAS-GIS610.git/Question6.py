import arcpy
arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb'
inFeatures = 'CallsforService'
fieldname = 'Crime_Explanation1'
field_type = 'text'
arcpy.AddField_management(inFeatures,fieldname,"TEXT")
featureClass = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\610 Exercise 3\Exercise 3.gdb\CallsforService'
fieldNames = ['CFSType','Crime_Explanation1']
with arcpy.da.UpdateCursor(featureClass, fieldNames) as cursor:
    for x in cursor:
        if x[0] == ('Burglary Call'):
           x[1] = 'This is a burglary'
           cursor.updateRow(x)
        print('row updated')


            



