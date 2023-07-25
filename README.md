-- Python Program to produce radarchart from a matrix competency --

**Purpose**
Radar chart for each dev (by family or for all competencies)
To compare profiles to a target profile

**Matrice of competency**
Name of competencies
Family of competencies
Level (1 to 5)

**Setting up**
All dependencies of this project are dealt by pip.
In order to retrieve all necessary dependencies, you need to:

- Install virtual env

  > > $ pip install virtualenv

- Activate venv :

# On Windows

> > $source env/Scripts/activate

(env)

# On Linux

> > $ source env/bin/activate

- Install all dependencies :

> > $pip install -r requirements.txt

-Configure your .env :

- Create your env file (from .env_EXEMPLE) with port and server adress

**Run project**

Go to /app and run :

> > $python3 app.py

and try all endpoints of 'app.py'

**Run tests**

> > $python -m unittest tests/test_functions.py
