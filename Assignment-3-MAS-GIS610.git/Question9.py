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

arcpy.AddField_management('Waves', 'ref_ID','TEXT') 


arcpy.env.workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

current_workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'

arcpy.env.overwriteOutput = True


domName = 'bluesClues'

arcpy.CreateDomain_management(current_workspace, 'bluesClues3','','TEXT','CODED')

domDict = {'BL':'Blue','GR':'Green','RD':'Red','PR':'Purple','YW':'Yellow'}

for code in domDict:
    arcpy.AddCodedValueToDomain_management(current_workspace,'bluesClues3',code,domDict[code])

arcpy.AssignDomainToField_management('Waves','ref_ID','bluesClues3')






