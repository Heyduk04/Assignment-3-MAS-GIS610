# Questions 1-4

1)	A property is the content of an object and if it is read/write, a method is the type of actions you can do with the object.
Example:  append() is a method will add an element or “property” to the end of a list 
	
2)	a. Property   =  	arcpy.env.overwriteOutput = True 
There are no parentheses meaning it is not a method.  
b. Method    =	arcpy.SearchCursor(“roads”, “TYPE” <> 4’) 
	It is a method because it is calling parameters ‘roads’,’TYPE’ and 4.
c. Method    =	row.setValue(‘distance’,100)   
	Similar to answer b. it is calling parameters to be used which makes it a method.
d. Property   =	ArcGISProject.dateSaved  
	There are no parentheses meaning it is not a method.  
e. Property   =	Table.isBroken 
	There are no parentheses meaning it is not a method.  


3)	Yes, two parameters are being passed into the function. 
‘String’ are the type of data being used. 
There would be no output as you haven’t invoked/called anything forward.  

4)	nameList = ['Michelangelo','Donatello','Raphael','Leonardo']
    def turtles(names):
    		for x in names:
	    		print(x + ' Happy Birthday. Give me some pizza!')
    turtles(nameList)	

