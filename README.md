# **Get Strong**

Get Strong is a training companion designed to assist you in creating, 
logging and reviewing your training regime.  
For years, I have been searching for a web app that allows me easily create a workout, 
review my progress and most importantly, 
log my workout easily while working out.  
I never found it!  
So, I will create it here.

## **Goal for this project**

To create an easy to use workout logging app which allows the creation of personalised workouts.
User will be able to review their progress over time and customise their workouts to fit their own objectives.
<a></a>

## Table of contents 
* [UX](#ux)
    * [Site Objective](#site-objectives)
    * [User Stories](#user-stories)
    * [Design](#design)
* [Wireframes](#wireframes)
* [Database Structure](#database-structure)
* [Features](#features)
* [Technologies used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

### **Site Objectives**
- build up a user-generated library of workouts people perform in their exercise routines
- allow a user to contribute to the database by adding their own workouts
- create an intuitive interface for users to add a workout easily
- allow an admin user to update the exercise choices and manage the site users
- give the user a profile page that displays workouts they have created

### **User Stories**
As a user, I would like to create a profile with my email and use it to login  
As a user, I would like to edit and update my profile  
As a user, I would like to create and customise my own workout regime  
As a user, I would like to log workouts easily  
As a user, I would like to create workouts of varying size/intensity for different days/objectives  
As a user, I would like to delete workouts/my profile  
As an admin user, I would like to see and manage the site users 
As an admin user, I would like to add/remove exercises to the list of available exercises for users to select

[Back to Top](#table-of-contents)

<a></a>

### **Design**

[Back to Top](#table-of-contents)

<a></a>

#### Colors

I used a simple color scheme to create contrast and also not to make the site look cluttered.  
I went with these colors as I will use a dark background image for the login page and this will keep with the color theme I'm aiming for.  
I utilised the color palette included in the materialise framework and chose two contrasting colors of deep-orange accent-3 and blue-grey darken-3 for the scheme

[Back to Top](#table-of-contents)

<a></a>

#### Fonts

For the fonts I decided to go with two contrasting fonts for different situations.  
I decided on the Condiment font on google fonts for titles as it's it's a little different
I decided on the Iceberg font on google fonts for everything else, as it's easy to read and will fit the theme of a workout log well

[Back to Top](#table-of-contents)

<a></a>

#### Structure
The app has a simple structure with only a few pages to navigate. The design is intended to be intuitive, so very little instruction is needed.

[Back to Top](#table-of-contents)

<a></a>


## **Wireframes**


#### Desktop Wireframes

![Dashboard desktop](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/dashboard_desktop.png?raw=true | height= 500)
![Log workout desktop](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/log_workout_desktop.png?raw=true)

#### Tablet Wireframes

![Dashboard tablet](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/dashboard_tablet.png?raw=true)  
![Log workout tablet](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/log_workout_tablet.png?raw=true)

#### Mobile Wireframes

![Dashboard mobile](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/dashboard_mobile.png?raw=true)   
![Log workout mobile](https://github.com/hjtb/Get-Strong/blob/master/website/static/wireframes/log_workout_mobile.png?raw=true)  



## **Database Structure**

I decided to utilise mongoengine so I could automatically implement validation and build my forms from my models using the modelform.  
This didn't come without it's own challenges and I had to learn on the job. 
I had to make a choice between embedding documents or not. 
I ultimately embedded the workout document inside the user document and went further down the   
rabbit hole by embedding the logExercise document inside the workouts.

I had previously worked with SQL databases so wanted to experiment with embedding.  

The types of data that are stored in the  database.
- Embedded Documents
- ObjectID
- Integer
- String
- Boolean
- Object
- Array

### **Non Embedded Route Which I didn't take**

Workout Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Workout Id|_id|ObjectId
Workout Name|name|String
Exercise|exercise|Select
Set|set|Integer
Reps|reps|Integer
Weight|weight|Integer
Comments|comments|String


Exercises Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Type ID|_id|ObjectID
Exercise|exercise|String


User Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID
Name|name|String
Password|password|Binary
Workout|workouts|array
Admin|admin|boolean

### **Embedded Route Which I made work**

#### User Collection:
```
{
    _id: ObjectID("stringofcharacters"),
    username: "string",
    password: "string",
    workouts: [
            {
             _id: ObjectID("object_ID_1"),
             workout_name: "string",
             exercises: [
             {
                     exercise_name: "string",
                     set: "integer",
                     reps: "integer",
                     weight:"integer"
             },
             {
                     exercise_name: "string",
                     set: "integer",
                     reps: "integer",
                     weight:"integer"
             },
             ...
     ],
    comments: "string"
    },
    .....
    ]
    is_admin: false
}
```

#### selectExercises Collection:
```
{
    _id: ObjectID("stringofcharacters"),
    Exercise name: "string"
}
```

[Back to Top](#table-of-contents)

<a></a>

## **Features**

### **Current Features**

#### Navbar
For the navbar icon I used a free logo from [www.vhv.rs](https://www.vhv.rs/) as they have a great selection of free logos for personal use. 
I also used this [stackoverflow](https://stackoverflow.com/questions/16116319/how-to-create-white-css-box-shadow) article to incorporate a white shadow and to ensure it works on all browsers.  

#### Flash Messages
For the flash messages I used and added some shadow and styling to make them stand out a bit more. 
I used this same [stackoverflow](https://stackoverflow.com/questions/16116319/how-to-create-white-css-box-shadow) article for the shadow. 

#### Login System 
Users can register an account and use it to login and all site functionality is login-protected

#### Add/Edit/Delete Workouts
Users can create workouts, update and delete them.   
Users can't see, edit other users workouts or profiles.  
Admin user can add exercises to the exercise collection in the MongoDB database.  

#### Edit/Delete Profiles
Users can update their profile information or delete their profile if they choose.
Admin users have extra privileges and can manage users of the site.  

[Back to Top](#table-of-contents)

<a></a>

### **Ideas for Future Features**

#### Templates
Add functionality to copy workouts to use as templates for other workouts

#### Privileges
Create functionality for admin users to escalate privileges for non admin users

#### Lost Passwords
Create functionality for if a user forgets their password - they can request to reset their password using their email

#### Calculate Calories/Volume
Add a calculator to return the amount of calories users burn/volume lifted during workouts.  

#### Statistics and graphs
add a log workout button to allow the user to say they did the workout on that day  
which will append the date to a list and store it as part of the workout object.  
This will allow users to track their progress.  
In future I will create a dashboard with a graph of user progress.  

#### Warning Modals
The delete functionality as it stands is problematic as one click deletes an object forever.  
i attempted to implement warning modals but couldn't pass the data to the modal and I ran out of time.  
I created a branch to pursue this further.  

[Back to Top](#table-of-contents)

<a></a>

## **Technologies used**

1. HTML and CSS were used to structure and style the app
2. Javascript was used to add and remove exercises rows dynamically on the workout forms and enable the workings of Materialize components
3. Python was used to write the app
4. [Materialize CSS](https://materializecss.com/) was used for styling and responsive design
5. [Gitpod](https://www.gitpod.io/) was the IDE used for the project
6. [Balsamiq](https://balsamiq.cloud/) was used to create the basic wireframes
7. [Github](https://www.github.com/) was used for version control
8. [MongoDB](https://www.mongodb.com/) stored all the data generated in the app
8. [Heroku](https://id.heroku.com/) was used to deploy the app
9. [Jquery](https://jquery.com/) was used to dynamically load forms and hide Flashed messages

[Back to Top](#table-of-contents)

<a></a>

### **Languages**

[Back to Top](#table-of-contents)

<a></a>


## **Testing**

### Security 

Throughout the development process, defensive design has been a key consideration. I have, so far, been unable to trigger any errors or unexpected behaviours by using the app normally or by attempting to get around the defensive measures.

Below is a table that details the key defensive design tests performed on the app and their outcomes. 

| Element/function to test | Expected outcome | Result |
| --- | --- | --- |
| Protection of links in navbar | The user should only be able to see a link to register or login if they are not logged in | Passed |
| Protection of all routes | If a user is not logged in, an attempt to access a protected view should redirect them to the login page and flash a message prompting them to login | Passed |
| Protection of admin specific view, link and functionality | If a non-admin user attempts to access the route and function that allows the admin user to add exercises to the database, they should be redirected back to their dashboard if logged in, or redirected to the login page if not logged in. Non-admin users cannot see the link to the protected view | Passed |
| Users can only access workouts that they have authored | Any attempt by a user to view a workout that they have not authored will result in a redirect to the dashboard and a flashed message informing them that they cannot access that workout | Passed |

### Responsiveness/Ease of use

The app has been tested on a variety of different devices and browsers.

1. iPhone XR

    - The app was tested on Safari, Firefox and Chrome and perfomed as intended vertical orientation. 

2. iPad Pro

    - The website was tested on Safari and performed as intended in both orientations

3. 21.5 inch iMac with 1080p display

    - The website performed as intended on Chrome and Safari

4. iPhone 5, 6/7/8, 6/7/8 plus, iPad, various android phones, laptops and a 4K monitor were all simulated in Chrome Developer Tools to check for responsiveness

    - All performed as intended; with simlutated mobile devices working well in vertical orientation

### Code Validation

All HTML and CSS was validated on the [W3C Markup Validation service](https://validator.w3.org/).   
All Python code was checked for syntax on [PythonChecker](https://www.pythonchecker.com/).  
javascript code was tested on [Esprima](https://esprima.org/demo/validate.html).  
No errors were shown in the HTML, CSS, JS or Python code.  

[Back to Top](#table-of-contents)

<a></a>

## **Deployment**

### Local Deployment

The project was started in Gitpod, then moved to VSCode and the repository is stored at Github.  
If you would like to clone the project to run locally on your machine,   
please follow the steps below:  

Going to the repository on Github  
Clicking on the "Code" button at the top right  
The link to be copied will then be displayed  
In your IDE, ensure you are in the correct directory and then type "git clone" followed by pasting the link  
The repository will then be cloned into your chosen directory.  

### Deployment on Heroku: 

The project is hosted by Heroku, and these are the steps to get it running.  

Log into Heroku and navigate to the dashboard  
Click on "New" in the top right corner and select "Create new app"  
Name the app and select the correct geographical region  
Click on the "Deploy" tab and select the Github deployment method  
Ensure Heroku and Github accounts are linked  
Enter the name of the repository into the field, search for the repository and connect it to the app  
Click on the settings tab and then "Reveal Config Vars"    
Input the config vars from the .env file (IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME)  
Navigat back to the "Deploy" tab and click "Enable Automatic Deploys"  
Select which branch to deploy from - master being the default   
Finally, click on "Deploy Branch"  
The repository contains the requirements.txt and Procfile necessary for deployment to Heroku.  
The terminal command to generate the requirements file was $ pip3 freeze --local > requirements.txt and  
the Procfile is created with the command echo web: python app.py > Procfile

If you are going to clone this repository and set up the app hosting with Heroku following the steps above, you will also need a .env file.   
The structure of this file is detailed below:  

```
IP = 0.0.0.0
PORT = 5000
SECRET_KEY = "**YOUR SECRET KEY HERE**"
MONGO_URI = "**YOUR MONGODB URI HERE**"
MONGO_DBNAME = "**YOUR MONGODB DATABASE NAME HERE**"
```
The MongoDB databse must be correctly configured as well:

Within the cluster, navigate to the "Collections" tab  
Create a new database named "get_strong"  
Create the appropriately named collections (detailed above)  
Follow the data models above and input some documents to get started  
On the left of the screen there is a link under the Security section titled "Database Access"  
Ensure that you have a user created with the ability to read and write to any database  
Navigate back to the overview of your clusters and click "Connect" on the right of the screen  
Click "Connect your application" and select the Python driver and correct version  
Copy the connection string, taking care to update the password and database name  
Paste this string in the .env file in the "MONGO_URI" section    
Input your database name in the "MONGO_DBNAME" section  
Your app should now be deployed on Heroku and talking to MongoDB correctly.  

You must also ensure that you have all the necessary modules installed in your IDE.  
This project relies heavily on third party modules for key functionality, and they are all listed below:   

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/) is the micro framework the project relies heavily upon - in the terminal use: ```$ pip3 install Flask```
2. [Flask-mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/) integrates Flask and WTForms with MongoDB - in the terminal use: ```$ pip3 install flask-mongoengine```
3. [Flask-Login](https://flask-login.readthedocs.io/en/latest/) is used to manage loggin in and out and to protect views and functions - in the terminal use: ```$ pip3 install flask-login```
4. [dnspython](https://pypi.org/project/dnspython/) is to enable usage of MongoDB connection string - in the terminal use: ```$ pip3 install dnspython```
5. [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) is used to debug during development and to generate hashed passwords - it comes as part of Flask so no extra installation commands are necessary
6. [dnspython](https://pypi.org/project/dnspython/) is to enable usage of MongoDB connection string - in the terminal use: ```$ pip3 install dnspython```


[Back to Top](#table-of-contents)

<a></a>

## **Credits**

Pretty Printed and freecodecamp on Youtube were instrumental in helping me understand backend form validation and mongoengine
Miguel Grinbergs The Flask Mega-Tutorial helped me understand the correct way to create an app with flask
Huge thanks to [Peter](https://github.com/pbs-websuntangled) from [dt-squad](https://www.dt-squad.com/) who was always there on hand for when things were falling apart, especially after git merges that go terribly wrong.
Thank you to my Code Institute mentor, Brian Macharia, he cleared up some of the complicated issues I was running into at the start. Thanks, Brian.
[Back to Top](#table-of-contents)

<a></a>







