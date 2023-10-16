## AirBnB clone - The console
This is the console application of the AirBnB web application clone.

### Description
In this repository we are implementing the console application of the AirBnB 
web application clone. Basically the console will take some basic commands and execute them. A file system was used for the storage of data.

### How to start the console
To start the console application use the command
 > ./console.py

### How to use the console
The console works with commands.
The following commands are currently handled by it.
`all`, `create`, `update`, `destroy`, `show`.

#### example
In order to print all the data stored in the storage engine
 > all
or 
 > all 'class name' 
to print objects of a particular class

In order to create and object and store it in the storage engine
 > create 'class name'

In order to update and save an existing object in the storage engine
 > update 'class name' 'id of object' 'attribute' 'value'

To destroy an object
 > destroy 'id of object'

To print an object
 > show 'class name' 'id of object'
