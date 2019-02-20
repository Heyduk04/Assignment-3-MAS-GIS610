import arcpy
current_workspace = r'C:\Users\theyduk\Desktop\Heyduk_LabWork\610 Assignments\MAS-GIS\Test.gdb'
geometry_type = "POLYGON"
spatial_reference = arcpy.SpatialReference
featureList = ['CapitalCities','Landmarks','HistoricPlaces','StateNames','Nationalities','Rivers']
arcpy.env.workspace = current_workspace
arcpy.env.overwriteOutput = True
def createFeatureClass(in_fc_name):
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
    print('Feature Class ' + in_fc_name + ' was sucessfully created.')
createFeatureClass('Geography')
featureList = ['CapitalCities','Landmarks','HistoricPlaces','StateNames','Nationalities','Rivers']
for x in featureList:
    createFeatureClass(x)





