# Getting Started - Django Rest Framework (DRF)

![](https://www.django-rest-framework.org/img/logo.png)
Django is a popular web development framework in Python. It helps you to create web based applications such as websites and web services. Django Rest Framework (DRF) is a powerful toolkit that helps you to create RESTful services with Django. It provide serialization support for ORM and non-ORM data models. It provides a browserable web ui that helps developers to run and test APIs. You can create function based views and class based views for your Django REST applications.

## Setting up Python Virtual Environment in VS Code
-------------
To create and run Django projects you can use a Virtual environment. Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application. In virtual environment you can create a `requirements.txt` to reproduce files of virtual environement  to another development environment. 

Follow the steps to setup the Django project in VS Code:
1) Create a folder  "eshop" in your development machine. 
2) Open command prompt and set "eshop" as current working directory
3) Run the following command to create a virtual environment 
	> `python -m venv env`
4) Open project folder in VS code by running 
	> code .
5) In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the `Python: Select Interpreter command`:
6) It lists the available Python interpreters in the current environment. It lists globally installed python and virtual environment python in `env` folder. Select the virtual env python. (`eg: .\env\Scripts\Python.exe`)
7) Open the integrated terminal .Ensure the default terminal type is `Command Prommpt`. It activates the Python environment using the activation script automatically.
8) Install Django and Django Rest framework (DRF) in the virtual environment by running one of the following commands in the VS Code Terminal:	
	> `python -m pip install django djangorestframework`
9) You now have a self-contained environment ready for writing Django code. VS Code activates the environment automatically when you use `Terminal: Create New Integrated Terminal`.

## Create a simple Django REST service project
In Django terminology, a "Django project" is composed of several site-level configuration files along with one or more "apps" that you deploy to a web host to create a full web application. A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects.

To create a minimal Django app, then, it's necessary to first create the Django project to serve as the container for the app, then create the app itself. For both purposes, you use the Django administrative utility, `django-admin`, which is installed when you install the Django package.

1) In the VS Code Terminal where your virtual environment is activated, run the following command:
	> `django-admin startproject eshopproject .`
2)  creates the following within it:
	* **manage.py**: The Django command-line administrative utility for the project. You run administrative commands for the project using python manage.py <command> [options].
	* A subfolder named `website`, which contains the following files:
		* **__init__.py**: an empty file that tells Python that this folder is a Python package.
		* **wsgi.py**: an entry point for WSGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.
		* **settings.py**: contains settings for Django project, which you modify in the course of developing a web app.
		* **urls.py**: contains a table of contents for the Django project, which you also modify in the course of development.
3) To test the project is created and running successfully, Open the terminal (make sure it is in python venv) and run the following command.	
	> `python manage.py runserver`
4) The project will run and the server will listen on localhost port number 8000. Open browser and navigate to the url.
	```Watching for file changes with StatReloader
	Performing system checks...

	System check identified no issues (0 silenced).

	You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, 
	auth, contenttypes, sessions.
	Run 'python manage.py migrate' to apply them.
	April 22, 2020 - 11:03:23
	Django version 3.0.5, using settings 'website.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.
	```
5) Close the browser and press `Ctrl+C` to stop the server.

## Building your first REST service using Django Rest Framework

1) Open Integrated Terminal in the 

