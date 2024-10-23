# Learning-Docker
This is simple project to study containers 

Comments, advices:
-------------------

First, good job :-)

1. try to use .gitignore file in your project and ask chatgpt how to use it
=> virtual environment folder is not ussually commited and pushed to remote github (it can be too big size.. and it is not neccessary, details in 2)
..ask chatgpt what is the best to ignore in .gitignore in your project

2. It is good practice to use in python project Pipfile and when using pipenv lock and pipenv install, it is also beneficial to commit and push to remote github both files Pipfile and Pipfile.lock instead of venv directory

3. Conventional commits types and documentation: https://www.conventionalcommits.org/en/v1.0.0/

4. docker permission during building the image - try to ask chatgpt for details about the error and if it is connected with using sudo of root user or in this moment the linux user is not in docker group and does not have therefore permissions..also find out in that case how to add user to docker group
=> you can ask chatgpt how to find out the actual used user in ubuntu


To run container I can use: docker run -it --rm --name my-running-app my-python-app

5. try to move functionality of uvicorn server to move that into python code..so try to ask chatgpt how to do it and maybe also what is better to do from those 2 possibilities in this case

6. in fast api, you have there one api enpoint, the root one with "/"..try to add some based on it which will be called "/now" and it will make get request to get UTC time and return that

7. try to make another endpoint "/search" where it can take query parameter..try to implement in this endpoint method the request to google.com and return the first link which it will find

8. try to make proxy enpoint, where will you have possibility to use 2 parameters in the path, for example "/proxyendpoints/{searched_thing}/{how_many_links}", where searched_thing can be string type and how_many_links integer type..you can ask chatgpt about the typing in endpoints and how to work with that..so for example when somebody will make request to localhost:8000/proxyendpoints/basketball/3, it will use that basketball and 3 and search in google 3 first links about basketball

Good luck and enjoy :)
///////////////////////////////
9) create another docker container with another application which will have running python application with mongodb or postgresql

10) this container will have another communication port

11) those 2 containers will be able to comunicate together via those ports

12) in the first container you will make endpoint that you can add items in the database in that second container,where database should be persistant,so if you will stop container,it will keep data in local disc somewhere where specified..

13) you can create some items in database manually or by some requests to it

14) EXTRA task - if you will have surplus for it, you can try to find out,how to define those containers in one docker-compose.yaml file

15) EXTRAEXTRA task - think about how to refactor this project in the files or folders if we have all this
////////////////////////////////
16) you have in app search..we need to have also other methods for:
    a) add to database
    b) remove from database
    c) update some existing item in database
    d) update some specific property of the item in database
17) very very basic UI, when for now on the webpage will be just textbox and button for that search
18)  also another one to write properties of the items to be added in database
19) ...also for editing of existing item
20) ...removing of existing item
...so the database model can be used in the form that you have
21) there can be possibility to add some property to database model, so maybe textbox and button
/////ideas for next tasks..
download some testing database with many items (10000?) and play with that to see what is fast/slow method
UNIT TESTS
PYDANTIC models usage
server is secure - https and one needs certificate to be able to get information
response modes, requests models
AWS
CI/CD pipeline