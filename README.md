# CSC2033 Team Project

## URL to GitHub repository

## Installation instructions

Clone the project from GitHub

URL to GitHub repository: https://github.com/squiree98/CSC2033_Team_Project

### Installing dependencies

- Create a new virtual environment
- Install the python packages specified in requirements.txt:

```
pip install -r requirements.txt
```


### Initialising the database

In the python console (in PyCharm), enter the following commands

```python
from models import init_db

init_db()
```
Note: You must be connected to the team database for the initialising of the database to be successful

### How to run the application

- Create a new configuration or edit configuration and set it to a python configuration.
- Set the Script path to the path for app.py in the project
- Run the application (click the green play button in PyCharm)
- Click the URL that appears in the terminal to launch the web application


