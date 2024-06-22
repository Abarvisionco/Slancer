# Slancer
A website to display the interns and students of the country's conservatories and select them by different companies for internships. This website was established to speed up the time to find a job or intern, It has an advanced chat room panel, and it is an idea by Abarvision.

>[!NOTE]
>The latest version is ready for project deployment.
>this repo is open source


[![Python](https://img.shields.io/badge/python-%2320232a.svg?style=for-the-badge&logo=python)](https://github.com//prodbygodfather)
[![Django](https://img.shields.io/badge/django-%2320232a.svg?style=for-the-badge&logo=django)](https://github.com//prodbygodfather)
[![Js](https://img.shields.io/badge/java%20script-%2320232a.svg?style=for-the-badge&logo=javascript)](https://github.com//prodbygodfather)
[![html5](https://img.shields.io/badge/html5-%2320232a.svg?style=for-the-badge&logo=html5)](https://github.com//prodbygodfather)
[![css3](https://img.shields.io/badge/css3-%2320232a.svg?style=for-the-badge&logo=css3)](https://github.com//prodbygodfather)



<img src="./static/images/fav.svg" width='200px'>

## Structure
Description of applications and project foldering
>- #### Karamooz
>  this is project and including settings and asgi files and main packages and main urls 

>- #### main
>  The main routers of the project include the main pages, the default settings of the project without facilities, etc.

>- #### resume
>  Users' resume settings, creating, deleting, displaying and updating their information are available in this application.

>- #### company
>  Users' company settings, creating, deleting, displaying and updating their information are available in this application.

>- #### users
>  User section settings and their models, SMS settings, etc.

>- #### chat
>  Employer and trainee chat room settings and routers

## Execution 
For better project execution, it is recommended to use a virtual environment. To install it: 
 
```
pip install virtualenv 
```
 
 
- Create a virtual environment: 
 
```
virtualenv venv 
 ```
 
 
- Activate the virtual environment: 
 
```
source venv/bin/activate 
 ```
 
 
- After activating the virtual environment, there is a `.txt` file containing the required libraries and frameworks embedded. Install it within the virtual environment: 
 
```
pip install -r requirements.txt 
 ```
 
 
- Once the project dependencies are installed, run the project: 
 
```
python manage.py runserver 
 ```
