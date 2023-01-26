# README

## An explanation of the organization and name scheme for the workspace 
The VerdeCars web app will be stored in a Github repository titled CS-3450-Group6-Project.  

All documentation and other resources will be put in another folder labeled “docs”. This includes our list of requirements, our project plan, our use case diagrams, and anything else we may need as we continue to build our project.  

The project will be kept in a folder called verdeCars. This is where we will keep our actual code files.  

## Version-control procedures
We use GitHub as our version control system. Each member of the team will make changes on their own branch. Another team member must approve the pull request for a branch to be merged onto master.  


## Tool stack description and setup procedure
Our tool stack will consist of our:
*Backend:* Python
* Specifically the Django framework which is used to process requests and upsert / retrieve calls to the database
*Database:* SQLite
* Used to process upserts and requests from Django for user information - this will store permission levels for each user
*Frontend:* Javascript, HTML5, MomentJS, Pikaday
* Javascript will be used for base functionality of buttons, and ajax calls
* MomentJS will be used as our date and time formatting 
* Pikaday will be used as our date selector paired with moment to more dynamically handle date objects  
* HTML5 is our markup language that will be used to create each web page.


## Build instructions

* Generate Secret Key 
    * Required for modifying server
* Run the following Database migrations:
    * 0001_inital.py
* `python manage.py runserver` to start the server



## Unit testing instructions
Unit tests have not been developed yet


## System testing instructions
System tests have not been developed yet


## Other development notes, as needed
None yet
