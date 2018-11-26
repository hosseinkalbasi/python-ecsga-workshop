
# Data Analysis and Python Development Workshop
#### Level: Beginner to Advanced
#### Instructor: Hossein Kalbasi
#### Place: Concordia University, Montreal, QC
#### Organizer: ECSGA (Engineering and Computer Science Graduate Students Association)
#### Objectives: 
* Learn Python Programming
* Analyze Data with Python
* Develop Web Application with Python


# Installation
install Anaconda https://www.anaconda.com/download/
* do not forget to add Anaconda path (checkmark) when installing Anaconda

install Visual Studio Code https://code.visualstudio.com/

install git  https://git-scm.com/



# Clone Repository
* open terminal and cd to your desired path
* enter: ```git clone https://github.com/hosseinkalbasi/python-ecsga-workshop.git```
* enter: ```cd python-ecsga-workshop```

Now you are inside the repository and have access to all the files.


# Create Python Virtual Environment and Install Jupyter Inside that (New Kernel):

open Anaconda Prompt and follow these steps:
(you can also use your terminal if conda is recognized - Anaconda path must have been added)

* go to your desired path (for example: c:\myfolder) using cd command (for instance: ```cd c:\myfolder```)

* make sure conda is recognized. enter: ```conda info```, and you should see some texts (information about conda package).

* enter: ```conda update conda```

* enter: ```conda create --name myenv python=3.7```

* enter: ```activate myenv``` (or ```source activate myenv``` for MacOS and Linux)

* enter: ```conda install pip```

* enter: ```conda install ipykernel```

* enter: ```python -m ipykernel install --user --name=myenv```

* enter: ```jupyter notebook```

* copy paste the generated token (URL) into a browser (if it didn't pop out to a browser itself)
* open a notebook and instead of Python 3 (as kernel) select myenv, you should be now inside your virtual environment
* confirm that you are inside your virtual environment by entering the following in your Jupyter Notebook:

```
import sys
print(sys.executable)
```
It should print the python path to your virtual environment (you should be able to see the name "myenv" in the path)
* good job! happy Python coding!

Useful link: Conda Cheat Sheet https://conda.io/docs/_downloads/conda-cheatsheet.pdf


# Data Analysis with Python
Refer to the repository. Look for files with .py and .ipynb extensions

# Python Development using Django
Refer to Python Development folder. The project structure is like this:

```
mysiteproj/
├── mysiteproj/
├── siteapp/
├── db.sqlite3
└── manage.py
```

* activate your virtual environment
* ``` conda install django == 2.1 ```

* cd to the first mysiteproj directory where manage.py file is

make sure migrations are done at Django:

``` python manage.py migrate ```

``` python manage.py makemigrations ```

``` python manage.py migrate ```

run the server

``` python manage.py runserver 8000 ```

enter ```localhost:8000``` into a browser and you should be able to see your web application


