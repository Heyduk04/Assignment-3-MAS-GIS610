import arcpy

arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

current_workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

geometry_type = "POLYGON"

spatial_reference = arcpy.SpatialReference

featureClass = ['Tsunami']

arcpy.env.overwriteOutput = True

def CreateFeatureClass(in_fc_name):
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
    print('Feature Class ' + in_fc_name + ' was sucessfully created.')

CreateFeatureClass('Waves')

featureClass = ['Tsunami']
for x in featureClass:
    CreateFeatureClass(x)

inFeatures = 'Waves'
fieldName1 = 'ref_ID'

arcpy.AddField_management('Waves', 'ref_ID',"LONG") 


#I was able to complete all the previous steps for Question 9, but continued to get errors regarding line 39 for domain name. 
#I've tried to redefine my domain name numerous times but was still unable to get the code to process.
arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

current_workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

arcpy.env.overwriteOutput = True

gdb = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'
domName = 'bluesClues'

arcpy.CreateDomain_management(current_workspace, gdb, 'bluesClues','TEXT','CODED')

domDict = {'BL':'Blue','GR':'Green','RD':'Red','PR':'Purple','YW':'Yellow'}

for code in domDict:
    arcpy.AddCodedValueToDomain_management(gdb,'bluesClues',code,domDict[code])

arcpy.AssignDomainToField_management('Waves','gdb','ref_ID','bluesClues')






