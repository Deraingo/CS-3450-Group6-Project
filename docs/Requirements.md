# Verde Cars Rent-A-Car

## Introduction and Context
This site is for Verde Cars, a rental car business that rents out only green cars. Customers must have an account with the site in order to rent a car. When renting a car, a customer can choose either a $10 car, a $50 car, or a $100 car.

## Users and their Goals
### Customer
1. Can rent a green car, either from the $10, $50, or $100 category, for 1+ full days.  
2. Given a check-out code to show the person at the till when they come to get their rental car.
3. When they return the car, they show their check-out code to the person at the till to check the car back in.
4. If they return the car late, the site will display a notification to them saying that they owe a late fee, and giving them an option to pay the fee (a button to push, probably).
5. Can add more money to their account.
6. Can report that their car has broken down (which will send the retrieval specialist to get the car) and type in the address they're at.

### Customer Service
1. Checks in customers (verifies that they're the right person, verifies what  car they've rented, gets them the keys and the car, checks the car in/out).
2. Can offer the customer "insurance" for $50.
3. If the customer denies the "insurance," the person at the till pushes a button that says to LoJack the car.
4. If a customer returns their car late, the site will display the late fee to the till worker for them to remind the customer about it.
5. Can log the amount of hours they've worked.
6. Takes code and enters it into their page to make sure it's a valid code
7. Paid $15/hr 

<!-- Profe said that the till person's page will probably look like a bunch of checkboxes -->

### Automobile Retrieval specialist
1. Can see what address a stuck customer is at.
2. Can report a car as having been picked up and taken back to the shop.
3. Can log the amount of hours they've worked.
4. Paid $15/hr 

### Admin
1. Can add a new vehicle. (Profe said we could give the admin a library of pictures to choose from of new cars to add.)
2. Can see how much money is owed to every employee.
3. Has a button to mass-pay all employees, but the option to opt-out any of the individual employees from beging paid.
4. Can promote/demote other users to any position (including admin).


## Functional Requirements (what the system must do)

-----
1. Keep track of money in users' accounts, as well as how much money the company has earned, how much is owed to employees, and how much is in the employees' accounts.  
2. The system has four different types of users (customer, till worker, retrieval specialist, and admin). When a user logs in (logging in is the way the site authenticates users) they can see different pages depending on the type of user they are.  
3. Keep track of what day it is and which cars are already being rented that day.  
4. Keep track of the rental period for each car that gets rented.  
5. The system calculates how much money is owed to each employee based on how many hours they've worked.  
6. Fine a user if they return their car late.  
7. Late return fee is twice the price of the rental.  
8. Two customers cannot order the same vehicle  - throw error if someone tries to checkout with vehicle after someone has rented it already
9. People who sign on have customer permissions by default  
10. Display today's date, and an option to display what the site would look like on another day - Moment, Pikaday   
11. Stop a customer from renting a car if they don't have enough money for it.
12. When a customer does a search, it should only show them the cars that are available to rent, but it /can/ show cars that the customer can't afford. 


### Insurance:
1. Costs $50.00
2. A customer can opt-out of buying insurance when they rent a car.
3. If they opt-out, the person at the till will secretly have the car LoJacked and it will break down.
4. If a car breaks down, the customer will have to pay $300 for the retrieval specialist to bring the customer a new car and take the broken one back.

[comment]: <> ( On the page where a user reports a car break-down, they could have the option of submitting an ethics violation to the better business buero about the insurance and LoJack situation if they want. The message would just go back to the company and get deleted though.)


## Non-functional Requirements (general properties of the system)  

1. Intuitive for customers  
2. Filter / sort methods for cars
3. (Could) Can add upload photos of cars

## Future Features
1. If the user gets a late fee and doesn't pay, they can't rent a car again until they pay their fee.
2. Employees get a discount on car rentals.
3. The system keeps track of available parking spaces at the shop so the retrieval specialist knows where they can park the retrieved cars.
4. (Could) Are given a QR code to show to the person at the till when they go to get their car. (Note to developers: could use an API to do this.)
Customers can check out more than one car.
<!-- * Customers can rent more than one car at a time -->

## Glossary
