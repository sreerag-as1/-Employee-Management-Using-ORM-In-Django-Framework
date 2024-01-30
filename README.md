# MyEmployeeManagerApp - Employee-Management-Webpage-Using-ORM-In-Django-Framework

## Overview
MyEmployeeManagerApp is a simple Employee Management Webpage developed using Python Django ORM. This project provides essential features for managing employee records, including creating, updating, deleting, and viewing a list of employees. The web application collects key employee details such as ID, name, age, salary, and address. MyEmployeeManagerApp consists of three main pages: Home, Employee Management, and Contact Us.

## Features
1. **Home Page:** Welcome page providing an introduction to MyEmployeeManagerApp.
2. **Employee Management Page:**
   - **Create Employee:** Add new employees to the database with their ID, name, age, salary, and address.
   - **Update Employee:** Modify existing employee information.
   - **Delete Employee:** Remove employee records from the system.
   - **View Employees:** Display a list of all employees with their details.
3. **Contact Us Page:** Connect with the project maintainers for any queries or feedback.

## Getting Started
Follow these steps to set up MyEmployeeManagerApp on your local machine:

1. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the Application:**
   Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to explore MyEmployeeManagerApp.

## Project Structure
- **myemployeemanagerapp/**
  - **settings.py:** Django project settings.
  - **urls.py:** Define project-level URLs.
- **employee/**
  - **models.py:** Define the Employee model.
  - **views.py:** Implement views for employee management.
  - **urls.py:** Define app-level URLs.
  - **templates/employee/:** HTML templates for employee-related pages.
- **templates/**
  - **home/:** HTML templates for the home page.
  - **contact/:** HTML templates for the contact us page.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## Contact Us
If you have any questions or feedback, please reach out to us:
- Email: myemployeemanagerapp@example.com
- Twitter: [@MyEmpManagerApp](https://twitter.com/MyEmpManagerApp)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Thank you for using MyEmployeeManagerApp!
