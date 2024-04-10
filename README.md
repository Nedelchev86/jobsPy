# JobsPy - LIVE DEMO [JobsPy](https://jobspy.eu)

JobsPy is a job portal designed to connect job seekers with companies. It provides a platform for job seekers to showcase their skills and for companies to advertise job openings and manage applications.
![main](https://github.com/Nedelchev86/jobsPy/assets/122647190/d8cf6df9-c9b2-441f-b6fc-7add2de84595)


## Features

- **User Authentication**: Utilizes Django's built-in authentication system for secure user registration and login.
- Login with Google and GitHub
![login](https://github.com/Nedelchev86/jobsPy/assets/122647190/59bc234d-caeb-424f-a287-3ad0d7aae9a8)


- **User Roles**: Supports two types of users: job seekers and companies.
  
  ![singUp](https://github.com/Nedelchev86/jobsPy/assets/122647190/aaf1dafa-867a-422f-85bc-9e32c2270923)

- **Job Seeker Profile**:
  - Personal Information: First name, last name, nationality, occupation, etc.
  - Social Links: LinkedIn, GitHub, personal website.
  - About: A brief description of the job seeker.
  - Education: Allows job seekers to add their educational background.
  - Skills: Job seekers can add their skills to their profile.

 ![jobseekers](https://github.com/Nedelchev86/jobsPy/assets/122647190/27c2c7f5-4a0d-43dd-9a79-55c8c12f116e)
 ![jobs1](https://github.com/Nedelchev86/jobsPy/assets/122647190/43a62956-29ee-4106-a9d4-9d36d2e95435)
 ![jobss2](https://github.com/Nedelchev86/jobsPy/assets/122647190/99b8efbe-05dc-486e-9cfc-c64464e303be)




  
- **Company Profile**:
  - Company Information: Name, description, location, email, website URL, etc.
  - Image: Option to upload a company logo or image.
    
![company_dashboard](https://github.com/Nedelchev86/jobsPy/assets/122647190/6eca838b-cc66-425b-b1ba-99c184cf3834)

    
- **Job Listings**:
  - Companies can publish job listings with details such as job title, description, requirements, etc.
  - Job seekers can search for and apply to job listings.
 
  ![jobsall](https://github.com/Nedelchev86/jobsPy/assets/122647190/ca6ba2f1-a487-47b2-8cca-a3bf77b9af19)

- **Application Tracking**:
  - Companies can track and manage job applications received for their listings.
  - Job seekers can view the status of their applications.
    ![applicant](https://github.com/Nedelchev86/jobsPy/assets/122647190/bb536aea-c91c-42e9-bc23-4b837a17b8be)



 
- - **Blog** with Django REST Framework
  - Create, read, update, and delete blog posts.
  - Add comments to blog posts.
  - Rich text editing for blog post content using CKEditor.
  - User authentication and authorization.
  - Pagination for blog posts and comments.
  - API endpoints for retrieving and manipulating blog posts and comments.
    ![blog](https://github.com/Nedelchev86/jobsPy/assets/122647190/57eb606f-f9f7-4673-918e-4d05738d6d54)
    ![Blog2](https://github.com/Nedelchev86/jobsPy/assets/122647190/31dedca4-34ce-48cb-85d2-0ea87a50a62c)

 
API Endpoints

  /api/blog/: List and create blog posts.
  /api/blog/<pk>/: Retrieve, update, or delete a specific blog post.
  /api/blog/<pk>/comments/: List and create comments for a specific blog post.
  /api/blog/<pk>/comment/<pk>/: Retrieve, update, or delete a specific comment.

![rest](https://github.com/Nedelchev86/jobsPy/assets/122647190/0ddf85b6-50c6-4684-9055-d4f3d8ff8abd)


## Newsletter
  Subscribe for newsletter ( Celery and Redis for sending mails )
![newsletter](https://github.com/Nedelchev86/jobsPy/assets/122647190/cb41ec38-b8f2-4ef2-98d1-0092bdae24f4)


## Contact From
  Send mail for confirmation to you and to admin ( Celery and Redis for sending mails )
![contactUs](https://github.com/Nedelchev86/jobsPy/assets/122647190/9ff11d8d-28b3-40d6-9666-2a1bc259f577)

  


## Technologies Used

- Django: Backend framework for building the web application.
- Python: Programming language used for backend development.
- HTML/CSS/JavaScript: Frontend technologies for user interface and interactivity.

## Make .env Files

See envSampe.txt


## Installation

To run JobsPy locally, follow these steps:

1. Clone this repository: `git clone https://github.com/Nedelchev86/jobsPy.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the development server: `python manage.py runserver`
6. Access the application at `http://localhost:8000`

   

## Contributors



## License


