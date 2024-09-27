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
