**Overview**

You have to create a Django Application which should be able to store information about different types of Pizza, then create an API interface that lists the information about all the different stored pizzas, and also be able to  interact with that information (such as edit or delete).

**Database**

PostgreSQL should be configured with the project. Our database should be able to store information about Pizza, following are the details :

- A Pizza can be of multiple types : Regular or Square
- A Pizza can be of multiple sizes : Small, Medium, Large, etc. (These are just examples, the user should be allowed to add any other size at any point of time)
- A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.), the choice of toppings should not be limited to the ones mentioned above, the user should be allowed to add any type of topping at any point of time)

**API**

- Create an API endpoint to create regular pizza and a square pizza.
- Create an API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
- Allow filtering the list of pizza returned by the API based on Size & Type of Pizza.
- Create an API endpoint that allow the user to edit or delete any pizza from the database.

**Errors & Validation**

- The API should return proper 40x codes when any kind of wrong input is sent to the API, the server should not return 500 errors.

**Documentation**

- Proper documentation for each of the API endpoints and the accepted response for each endpoint should be mentioned in a README file on the repo.
- Include the steps to run the project as well

**Submission Guidelines**

- Code should properly be committed to the Git repository, then push to project to a public GitHub Repository and provide us with the link to it
- Requirements.txt for the project should be included as well, which will include the list of dependencies of the project with their version number along with it. (Hint: This file is created using the pip freeze command)
- Do not upload zip files to the GitHub repository and submit the links to it.