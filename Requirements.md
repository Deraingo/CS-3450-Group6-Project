***DOCUMENT IN PROGRESS***
***I WILL MAKE THIS SO MUCH PRETTIER and more organized I PROMISE***

Verde Cars (Rent-a-Car)

requirements: 3 car types ($10 small, $50 medium, $100 large) (all only green)
person at the till offers customer insurance
	customer can accept or deny insurance
	if they deny insurance, person at the till pushes a button that says to low-jack the car
	if a car is late the site will display the late fee to the till worker
		the site also puts a notification on the user page saying they owe a late fee and giving them the option to pay
	COULD: if the user doesn't pay (the late fee), they can't rent again until they pay
login for the till worker that takes them to their own page
at the beginning of the day, the program looks through all the checked-out cars and if any are overdue it fines them

customer page:
	- get a qr code (use an API for this) when you check out a car to show the person at the till
	- use that same qr code to check in the car when they're done
	- be able to reserve cars by the day
	- can only rent a car if it's available

person will log into the page
depending on the permissions the person has, they can see various pages on the site


diff. types of users: admin, employee (till worker, retrieval specialist), customer
authentication for those users

employees put in the hours they've worked (by hand)
system calculates how much money that would amount to
admin has a page that shows how much money is owed every employee
	admin has a mass-pay button to pay everybody, but the option of opting out an individual employee
	can promote/demote other users to different positions
COULD: employees get a car discount
	


COULD: retrieval specialist parks the retrieved cars
	the site keeps track of available parking spaces

money system (admin pays, people can add more money)

USER:
	user page has a drop-down menu of different things they can do:
		add money to their account
		
