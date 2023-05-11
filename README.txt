"ATTRITIONGUARD"

Overview -
            In this employee attrition prediction project, historical data on employees, 
            such as demographic information, job-related factors, performance metrics, 
            and satisfaction levels, is collected and used to train a machine learning model.
            The model can then be used to predict the probability of an employee leaving 
            the organization based on their current information.


Project Structure -


ATTRITIONGUARD/
|   |
|   ├── AttritionGuard/
|   |   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
├── static/
│   │   ├── css
│   │   ├── datasets
│   │   ├── images
│   │   ├── images
│   │   ├── js
│   │   ├── login
│   │   └── register
├──templates/
│   │   ├── 
│   │   ├── about.html
│   │   ├── attrition.html
│   │   ├── attritionpredict.html
│   │   ├── contact.html
│   │   ├── index.html
│   │   ├── login.html            
│   │   ├── nav.html
|   |   ├── register.html
|   |   └── service.html
├── User/
│   |   ├── _pycache__
|   |   ├── migrations
|   |   ├── __init__.py
|   |   ├── admin.py
|   |   ├── apps.py
|   |   ├── models.py
|   |   ├── tests.py
|   |   ├── urls.py
|   |   └── views.py
├── db.sqlite3
├── manage.py
├── READEME.txt
└── requirements.txt

Prerequisites-

    Python 3.10.10
    Django 4.1.7
    Anaconda 22.9.0

Installation-
    
    1.Run below command to create a virtual environment in the root directory of your project on anaconda prompt-> 
              conda create --name <virtual_environment_name> 

            -This will create a new virtual environment in a directory

    2.Run below command on anaconda prompt to Activate the virtual environment -> 
              conda activate <virtual_environment_name> (on Windows).


    3.Run below command to Install the required dependencies -> 
              conda install --file requirements.txt or pip install -r requirements.txt

    4.Run below command to deactivate virtual environment after use -> 
              conda deactivate or deactivate


Running the Project-

    1.To run the server use command -> 
              python manage.py runserver

    2.Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.

