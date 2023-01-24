# REST API implementation using Django Framework


Outcomes from this module included:

- Developed an understanding of the requirements' analysis process
- Introduced to systems design concepts such as use cases/sequence diagrams/class diagrams
- Created basic UML diagrams
- Applied SOLID principles using MVT (Mode, View and Template) architectural pattern
--------------------------------------------------------------------------------

## Requirements

### Business Requirements 

Vending machines can be very profitable. If you can get 
products to stock machines at good prices, and your vending 
machine is in a place that a lot of people go to, you can make 
a decent amount of money with little investment and time.

### User Requirements

- The user shall be able to create new task item.
- The user shall be able to view all the tasks.
- The user shall be able to update a particular task.
- The user shall be able to delete item.
- The user shall be able to upload CSV file and the data shall be stored.

### Specification

- Creating a task:
A user should be able to create a new task by making a POST request to the API 
with the task's title, start date and end date. The API should validate the request payload 
and return a response indicating whether the task was created successfully.
- Retrieving tasks: 
A user should be able to retrieve their list of tasks by making a GET request to the API. 
The API should return a list of all tasks, sorted by due date and Paginated.
- Updating a task:
A user should be able to update a task by making a PUT request to the API with the 
task's ID and any updated information (e.g., title, start date, end date). 
The API should validate the request payload and return a response indicating whether the update was successful.
- Deleting a task: A user should be able to delete a task by making a DELETE request to 
the API with the task's ID. 
The API should return a response indicating whether the delete was successful.
- Import endpoint: the user should be apple to upload a csv file where each row 
contains three columns that represent the task title , 
start date and end date respectively, and insert that to the system database.
### Diagram:
- **Use Diagram:**

![](figures/use_case.png)

- **Activity Diagram:**

![](figures/activity_diagram.png)


#### Functional Requirements

### Non-Functional Requirements
- The system must be  maintainable.
- The system must be higher reliability.

--------------------------------------------------------------------------------

## Design & principle

- MVT (Model, View and Template):


### UML Diagrams


- **Class Diagram:**

![](figures/class_diagram.png)



- **State Diagram:**

![](figures/state_diagram.png)

--------------------------------------------------------------------------------

## Implementation




--------------------------------------------------------------------------------

## Testing


To run the test. You can use the following commands:

```python
"""

test method - 

"""
python -m unittest
```
## Example
The following example from the run of the main class:
![](figures/example.png)




















