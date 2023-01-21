***DOCUMENT IN PROGRESS***

# Verde Cars Rent-A-Car

## Introduction and Context
This site is for Verde Cars, a rental car business that rents out only green cars. Customers must have an account with the site in order to rent a car. When renting a car, a customer can choose either a $10 car, a $50 car, or a $100 car.

QUESTION: DO WE WANT CUSTOMERS TO BE ABLE TO RENT MORE THAN ONE CAR AT A TIME?

## Users and their Goals
### Customer
* Can rent a green car, either from the $10, $50, or $100 category, for 1+ full days. 
<!-- NOTE: PROFE SAID THIS ^^^ FEATURE IS A 'COULD' WHEN WE WERE BRAINSTORMING AS A CLASS, SO WE COULD PUT THIS IN FUTURE FEATURES IF WE WANT -->
* When they return the car, they show that same QR code to the person at the till to check the car back in.
* If they return the car late, the site will display a notification to them saying that they owe a late fee, and giving them an option to pay the fee (a button to push, probably).
* Can add more money to their account.
* Can report that their car has broken down (which will send the retrieval specialist to get the car) and type in the address they're at.

### Customer Service
* Checks in customers (verifies that they're the right person, verifies what  car they've rented, gets them the keys and the car, checks the car in/out).
* Can offer the customer "insurance" for $50.
* If the customer denies the "insurance," the person at the till pushes a button that says to LoJack the car.
* If a customer returns their car late, the site will display the late fee to the till worker for them to remind the customer about it.
* Can log the amount of hours they've worked.
* Takes code and enters it into their page to make sure it's a valid code
* Paid $15/hr 

<!-- Profe said that the till person's page will probably look like a bunch of checkboxes -->

### Automobile Retrieval specialist
* Can see what address a stuck customer is at.
* Can log the amount of hours they've worked.
* Can check out cars to give customers a replacement
* Paid $15/hr 

### Admin
* Can add a new vehicle. (Profe said we could give the admin a library of pictures to choose from of new cars to add.)
* Can see how much money is owed to every employee.
* Has a button to mass-pay all employees, but the option to opt-out any of the individual employees from beging paid.
* Can promote/demote other users to any position (including admin).


## Functional Requirements (what the system must do)

-----
* Keep track of money in users' accounts, as well as how much money the company has earned, how much is owed to employees, and how much is in the employees' accounts.  
* The system has four different types of users (customer, till worker, retrieval specialist, and admin). When a user logs in (logging in is the way the site authenticates users) they can see different pages depending on the type of user they are.  
* Keep track of what day it is and which cars are already being rented that day.  
* Keep track of the rental period for each car that gets rented.  
* The system calculates how much money is owed to each employee based on how many hours they've worked.  
* Fine a user if they return their car late.  
* Late return fee is twice the price of the rental.  
* Two customers cannot order the same vehicle  - throw error if someone tries to checkout with vehicle after someone has rented it already
* People who sign on have customer permissions by default  
* Display today's date, and an option to display what the site would look like on another day - Moment, Pikaday   
* Stop a customer from renting a car if they don't have enough money for it.
* When a customer does a search, it should only show them the cars that are available to rent, but it /can/ show cars that the customer can't afford. 


###Insurance:
* Costs $50.00
* A customer can opt-out of buying insurance when they rent a car.
* If they opt-out, the person at the till will secretly have the car LoJacked and it will break down.
* If a car breaks down, the customer will have to pay $300 for the retrieval specialist to bring the customer a new car and take the broken one back.

[comment]: <> ( On the page where a user reports a car break-down, they could have the option of submitting an ethics violation to the better business buero about the insurance and LoJack situation if they want. The message would just go back to the company and get deleted though.)


## Non-functional Requirements (general properties of the system)  

* Intuitive for customers  
* Filter / sort methods for cars
* (Could) Can add upload photos of cars

## Future Features
* If the user gets a late fee and doesn't pay, they can't rent a car again until they pay their fee.
* Employees get a discount on car rentals.
* The system keeps track of available parking spaces at the shop so the retrieval specialist knows where they can park the retrieved cars.
* (Could) Are given a QR code to show to the person at the till when they go to get their car. (Note to developers: could use an API to do this.)
Customers can check out more than one car.
## Glossary


## Here are the requirements we've identified so far that aren't organized yet: vvv
login for the till worker that takes them to their own page

(non-functional requirement? vvv)
at the beginning of the day, the program looks through all the checked-out cars and if any are overdue it fines them

customer page:
	- can only rent a car if it's available

USER:
	user page has a drop-down menu of different things they can do:
		add money to their account
		
