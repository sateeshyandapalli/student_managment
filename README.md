# student_managment

the project able to handle CRUD Operations of a student

The list of endpoints 

1. createStudent
	Method: POST
	Url: http://localhost:5000/createStudent

2.getStudent 
	Method: GET
	Url: http://localhost:5000/getStudent?id=0006124485

3.deleteStudent 
	Method: GET
	Url: http://localhost:5000/deleteStudent?id=0006124485

4.updateStudent 
	Method: POST
	Params: json
	RequestBody: {"id": "0043280234","last_name": "y"}
	Url: http://localhost:5000/updateStudent

5.exportStudents
	Method: GET
	Url: http://localhost:5000/exportStudents
