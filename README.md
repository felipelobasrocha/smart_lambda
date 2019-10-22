****************************************************
- Interface Layer
 - It contains all the implementations to access the application
 - It uses the Port and Adapter Pattern

- Application Layer
 - It contains the application itself
 - Orchestration
 - Here it is defined all the application logic
 - It is the application "glue"

- Domain Layer
 - It contains the domain and business logic
 - The rules here are defined by Business People
 - It is the application's core and main reason to exist

- Infrastrucure Layer
 - It contains the application's technology
 - The technologies and rules here are defined by Software Architects and Software Engineers
 - It uses the Port and Adapter Pattern
****************************************************
****************************************************
Executing Console Application

- Open a terminal
- #cd {workspace}/scalable_example
- #python app.py [service_type account_type account_number money]
****************************************************
****************************************************
Executing Flask Application

- Open a terminal
- #cd {workspace}/scalable_example/example/interface/rest/flask
- #python -m flask run
- Open http://127.0.0.1:5000/ or the link showed in Terminal 
****************************************************