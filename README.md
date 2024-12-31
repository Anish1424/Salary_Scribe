**#Salary Scribe- Project Documentation**

**📋 Project Overview**
Salary Scribe is an full-scale payroll salary sheet management application designed to calculating and automate the calculation of employee salaries. It provides detailed employee information, computes various components like basic salary, allowances, bonuses and taxes and generates comprehensive salary sheets. The application also ensures compliance with tax regulations and provides performance-based bonuses. With its user-friendly interface and modular structure, Salary Scribe enhances efficiency, transperancy and accuracy in payroll processing, making it an invaluable tool for HR and accounting departments.

**🧑‍💻 Name of Contributors**
1. Dawkhar Anish Vilas
2. Gade Chaitanya Santosh
3. Shinde Anushka Sanjay
4. Walave Siddhant Dattatraya

**📋 Phases of the Salary Scribe Project**

 **Phase 1 : Planning:** The purpose of Salary Scribe project is to create a robust, efficient, and accurate payroll management tool that automates salary calculations, ensures compliance, enhances efficiency, improves accuracy, incorporates performance-based incentives, and generates comprehensive salary reports. It helps to address the critical needs of HR and accounting departments, making payroll management simpler and more reliable.
 
**Phase 2 : Creating Project Structure:** Discussing a functional requirements needed for creating structure and flow of application which helps in implementing a codebase structure.
	salary_scribe/ 
        main.py 
        employee/ 
            __init__.py 
            employee.py 
        salary/ 
            __init__.py 
            salary.py 
            salary_details.py 
            salary_sheet.py 

**Phase 3 : Coding and Implementation:** Phase 3 represents actual coding parts which transformed the structure and prototyes into actual implementation. Building each class within single package ensures the scalability and efficiency ensuring it meets out requirements. Within Salary_scribe package two more Sub-packages are created using __init__.py file inserting into it. While sub-package employee contains employee class including features of employee like employee_id , employee_name , employee_designation and employee CTC or montly salary. In salary sub-package three modules are created including salary,salary_sheet amd salary_details. 
Salary_sheet.py calulates net_salary , gross_salary from salary_details module and displays calculated salary components.
Salary_details.py includes actual implementation of function net_salary and gross_salary
Salary.py calculates montly_salary and annual_salary

**Phase 4: Testing :** This phase is crucial for identifying and fixing any bugs or issues that may have been missed during coding, ensuring that the applications delivers a seamless experience to users upon release.
This testing phase aims to:
•	Identify and resolve bugs in various parts of the application.
•	Ensure that all features perform as expected.
•	Optimize performance for a smooth user experience.
•	Align application performance with user expectations and project requirements.

**Phase 5: Deployment and Documentation :** Deploy the application to the desired environment and Monitor the application’s performance and handle any issues or updates. This deployment phase ensures the app is not only launched but also equipped for sustained user satisfaction through ongoing support and performance optimization, setting it up for long-term success.

**🔹Technical Requirements:**
	An Integrated Development Environment (IDE) such as PyCharm, VS Code, or any other preferred IDE.
	Version control system like Git for managing code changes.
	User input validation

**Steps to run:**
    1] Open Terminal
    2] Change directory to project folder
    3] Enter the command: python file_name.py
    4] Enter the input in the console
    5] Verify the results.

[Salary Scribe.docx](https://github.com/user-attachments/files/18282421/Salary.Scribe.docx)












