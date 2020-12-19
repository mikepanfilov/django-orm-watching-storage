# Django ORM watching storage

It is internal repository for 'Shining' bank stuff. If you got here by accident you is not able to lauch it because you have not enough DataBase permissions. But you can freely use this code or can look how DB requests are realized.

This script manipulates with visits data. Control center for security purposes.

### How to install

Install and activate virtual environment for project isolation. For example you can use this [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

### Example

Don't forget to activate virtual environment and install all dependecies.

Also you should make .env file and put folowings into it:
```
DB_ENGINE=django.db.backends.<desired_engine>
DB_HOST=<hostname or IP>
DB_PORT=<port number>
DB_NAME=<database name>
DB_USER=<database user name>
DB_PASSWORD=<database user password>
DJ_DEBUG=<debugging mode True or False>
```

Standard run:

```bash
$ python manage.py runserver

  * Performing system checks...

  * System check identified no issues (0 silenced).
  * December 10, 2020 - 01:39:53
  * Django version 1.11.29, using settings 'project.settings'
  * Starting development server at http://0.0.0.0:8000/
  * Quit the server with CONTROL-C.
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).