# README

## Link to the powerpoint on this project:
https://docs.google.com/presentation/d/1JRnQyBxS2UT89FsGWP7gUmssqfQrxzCK0izTyRyLzfc/edit?usp=sharing 

## Accessing the Full Site
To make the website functional, an admin of the website must be created. To do this, the user can use their superuser password to log in to Django’s built-in admin site. From here, they can either create or update a user, setting their UserType to “Admin.” After saving the user, there will be an admin connected to the site that can now keep track of the website’s money.

## Potential Issue When Running
When running the server there has been some randomness in how it runs.   
If there is an issue with running a page where it says it does not exist but you are sure it does go to urls.py in the application directory and remove the trailing `/` that should resolve any issues.  
We are currently trying to find a permanent fix to this 

## Testing 
There has been a carFill.py script made to do database management and testing so that we can test different kinds of cars and conditions on the database

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

* Add the Secret Key to settings.py
    * Required for modifying server
* Run `python manage.py migrate`
* `python manage.py runserver` to start the server
* It should be noted that the valid User types are "Customer", "Customer Service", "Retrieval Specialist", and "Admin"



## Unit testing instructions
Unit tests have not been developed yet


## System testing instructions
System tests have not been developed yet


## Other development notes, as needed
None yet

