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

### **User Stories**
As a user, I would like to create a profile with my email and use it to login  
As a user, I would like to create and customise my profile  
As a user, I would like to create and customise my own workout regime  
As a user, I would like to log workouts easily  
As a user, I would like to see my progress over time by viewing my previous workouts  
As a user, I would like to delete workouts/logs/my profile  
As a user, I would like to see other users workouts  
As a user, I would like to search exercises to add to my workout and add my own  

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
I decided on the Condiment font on google fonts for displaying messages to the user and reporting to the user
I decided on the Iceberg font on google fonts for everything else, as it's easy to read and will fit the theme of a workout log well

[Back to Top](#table-of-contents)

<a></a>

#### Structure

[Back to Top](#table-of-contents)

<a></a>


## **Wireframes**


#### Desktop Wireframes

[Dashboard desktop](static/wireframes/dashboard_desktop.png)  
[Log workout desktop](static/wireframes/log_workout_desktop.png)

#### Tablet Wireframes

[Dashboard tablet](static/wireframes/dashboard_tablet.png)  
[Log workout tablet](static/wireframes/log_workout_tablet.png)

#### Mobile Wireframes

[Dashboard mobile](static/wireframes/dashboard_mobile.png)   
[Log workout mobile](static/wireframes/log_workout_mobile.png)  



## **Database Structure**

The types of data that are stored in the  database.
- ObjectID
- String
- Boolean
- Object
- Array
- Binary


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


[Back to Top](#table-of-contents)

<a></a>

## **Features**

[Back to Top](#table-of-contents)

<a></a>

### **Current Features**

#### Navbar
For the navbar icon I used a free logo from [www.vhv.rs](https://www.vhv.rs/) as they have a great selection of free logos for personal use. 
I also used this [stackoverflow](https://stackoverflow.com/questions/16116319/how-to-create-white-css-box-shadow) article to incorporate a white shadow and to ensure it works on all browsers.  

#### Flash Messages
For the flash messages I used and added some shadow and styling to make them stand out a bit more. 
I used this same [stackoverflow](https://stackoverflow.com/questions/16116319/how-to-create-white-css-box-shadow) article for the shadow. 

[Back to Top](#table-of-contents)

<a></a>

### **Ideas for more Features**



[Back to Top](#table-of-contents)

<a></a>

## **Technologies used**

[Back to Top](#table-of-contents)

<a></a>

### **Languages**

[Back to Top](#table-of-contents)

<a></a>

### **Libraries and Frameworks**


### **Tools**


[Back to Top](#table-of-contents)

<a></a>


## **Testing**

#### As a user, I want to 

* **Goals**    

* **Method**   

* **Test**   

* **Results**    

[Back to Top](#table-of-contents)

<a></a>

## **Bugs**

* **Bug**  
https://stackoverflow.com/questions/29963847/select-element-doesnt-work-after-clone
* **Fix**

[Back to Top](#table-of-contents)

<a></a>

## **Deployment**

### Local Deployment
    
### Deployment on Heroku: 
   

[Back to Top](#table-of-contents)

<a></a>

## **Credits**

[Back to Top](#table-of-contents)

<a></a>







