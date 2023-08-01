-- Python Program to produce radarchart from a matrix competency --

**Purpose**

- visualize a radar chart with skills of a dev
- download a zip with a radar or polarbarchart (depending on the number of skills) by family of skills
- get a ranking of devs compared with a target dev (based on score of skills)

**Matrice of competency**
Name of skills
Family of skills
Level (1 to 5)

**Setting up**
All dependencies of this project are dealt by pip.
In order to retrieve all necessary dependencies, you need to:

- create your virtual env

> > python<version> -m venv <virtual-environment-name>

- Activate venv :

# On Windows

> > $source env/Scripts/activate

(env)

# On Linux

> > $ source env/bin/activate

- Install all dependencies :

> > $pip install -r requirements.txt

-Configure your .env :

- Create your env file (from .env_EXEMPLE) with port and host

**Run project**

> > $python3 main.py

and try all endpoints of 'main.py'

**Run tests**

> > $python -m unittest tests/test_functions.py
