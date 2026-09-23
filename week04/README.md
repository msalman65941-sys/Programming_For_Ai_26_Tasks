# Programming for AI — Week 4 Lab

## Topics Covered

* Object-Oriented Programming
* Classes and objects
* Constructors
* Attributes and methods
* Validation and encapsulation
* Inheritance and method overriding
* CSV file handling
* Text file handling
* JSON file handling
* Exception handling
* AI experiment tracking

## Reflection

### 1. How does a class improve organization compared with unrelated variables and functions?

A class keeps related data and functions together in one structure. For example, the Student class stores the student's SAP ID, name, and marks together and also provides methods for calculating the average, grade, and profile. This makes the program more organized and easier to reuse.

### 2. Why must custom objects be converted before they are saved as JSON?

JSON supports basic data types such as strings, numbers, lists, dictionaries, booleans, and null. A custom Python object cannot normally be stored directly in JSON. Therefore, the Experiment object is converted into a dictionary using the to_dictionary() method before saving it.

### 3. When is composition or a function clearer than inheritance?

Inheritance is useful when one class is a specialized type of another class and has an "is-a" relationship. Composition or a normal function can be clearer when objects simply use another object or when there is no strong parent-child relationship.
