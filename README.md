# ZotClassMobile: Backend

## TLDR:

- **Challenge**: Many lack support and guidance in having UCI course information on their mobile devices.
- **Solution**: ZotClassMobile, a tool that guides UCI collegiates in finding course information easily on their mobile devices.
- **Features**:
  - PeterPortal API information access.
  - User-friendly Home Screen to search for course information.
  - Apple and Android friendly

## The Problem

We got our inspiration from ZotCourse, which is a popular class scheduler for students at UCI. We wanted create an application that is able to show class information for students. When a student tries to search up their classes in ZotCourse or WebReg on their mobile browser, the interface feels scrunched and uncomfortable. 

## The Solution

With Zot Class Mobile, students do not have to go into a browser and look up their classes from there. Instead, they can just have an app on their phone that just shows the class information.

## The Inspiration

We got our inspiration from ZotCourse, which is a popular class scheduler for students at UCI. We wanted create an application that is able to show class information for students.

## How We Built It

- **PeterPortal API**: We started off communicating with the frontend on what we wanted to build, and we decided on making a mobile app that used information from the PeterPortal API. We created our own API based on information from PeterPortal.

- **Flask**: The backend started out with a flask and we used it as a framework to make API routes. We assigned these API routes to certain functions that accessed certain structures of information. Based on what the frontend imputed to us, we would find what information fit the requirements for that input and return all the information associated with it.

- **Efficient Filtering**: After we were able to organize the information based on certain requirements, we then had to sort the information we wanted from the information we didn’t want. We utilized for loops to access nested structures in order to find the information inside each object and we returned what we found back inside the function we used to send to the front end.

- **Public Deployment**: We also utilized gunicorn and git to deploy the code on Heroku so that our code was accessible outside our single laptop.

## Accomplishments

1. **Public Deployment**: Being able to deploy the code onto a public onto Heroku. It was my first step into making the project available and accessible to the public and not just on my local device.

## What We Learned

- Access data from a public API.
- Using Flask to build API routes.

## What's Next for ZotClassMobile

1. **Search Terms**: For the backend, we want to be able to implement more search terms that the user is able to include to further narrow their search. Due to the lack of time, we were forced to determine for ourselves the most important search terms for classes and did the best we could. If we had more search items in our database, we better utilize nested structures and ultimately a more effective and efficient search process for the user.
   
ZotClassMobile stands as a testament to technological innovation in UCI collegiate support, emphasizing the need for ease-of-access and understanding in digital solutions.
