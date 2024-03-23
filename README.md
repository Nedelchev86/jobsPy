# JobsPy

JobsPy is a job portal designed to connect job seekers with companies. It provides a platform for job seekers to showcase their skills and for companies to advertise job openings and manage applications.
![main](https://github.com/Nedelchev86/jobsPy/assets/122647190/d8cf6df9-c9b2-441f-b6fc-7add2de84595)


## Features

- **User Authentication**: Utilizes Django's built-in authentication system for secure user registration and login.
  ![login](https://github.com/Nedelchev86/jobsPy/assets/122647190/01e8c997-072e-45ff-8b15-97f9f6bcb719)

- **User Roles**: Supports two types of users: job seekers and companies.
  
  ![singUp](https://github.com/Nedelchev86/jobsPy/assets/122647190/aaf1dafa-867a-422f-85bc-9e32c2270923)

- **Job Seeker Profile**:
  - Personal Information: First name, last name, nationality, occupation, etc.
  - Social Links: LinkedIn, GitHub, personal website.
  - About: A brief description of the job seeker.
  - Education: Allows job seekers to add their educational background.
  - Skills: Job seekers can add their skills to their profile.
- **Company Profile**:
  - Company Information: Name, description, location, email, website URL, etc.
  - Image: Option to upload a company logo or image.
    
![company_dashboard](https://github.com/Nedelchev86/jobsPy/assets/122647190/6eca838b-cc66-425b-b1ba-99c184cf3834)

    
- **Job Listings**:
  - Companies can publish job listings with details such as job title, description, requirements, etc.
  - Job seekers can search for and apply to job listings.
- **Application Tracking**:
  - Companies can track and manage job applications received for their listings.
  - Job seekers can view the status of their applications.

## Technologies Used

- Django: Backend framework for building the web application.
- Python: Programming language used for backend development.
- HTML/CSS/JavaScript: Frontend technologies for user interface and interactivity.

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


