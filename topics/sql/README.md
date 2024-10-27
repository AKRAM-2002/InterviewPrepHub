# Introduction to SQL

Welcome to the **SQL Assignments** section! Here, you will find a series of assignments that will help you practice core SQL concepts through the famous **HR database** example, widely used in educational materials and practical SQL exercises.

SQL (Structured Query Language) is the standard language used for managing and manipulating relational databases. It enables you to create, read, update, and delete data (CRUD operations), as well as perform complex queries to retrieve and analyze information. Understanding SQL is crucial for anyone looking to work with databases, as it forms the backbone of data-driven applications.

## About the HR Database

The **HR database** is a widely-used educational database schema that contains tables like `employees`, `departments`, `jobs`, and `locations`. It simulates a company's HR system, making it ideal for practicing a variety of SQL operations, such as joins, triggers, stored procedures, and more.

In these assignments, we will explore the HR database to perform tasks ranging from simple data insertion to advanced operations like writing triggers and stored procedures.

## List of Assignments

Here are the 10 assignments that will help you master SQL concepts through practical scenarios:

1. **[Data Insertion and Foreign Keys](./assignment-1-data-insertion-foreign-keys/README.md)**  
   *Task*: Insert data into the `employees`, `departments`, and `locations` tables while handling foreign key relationships.  
   *Goal*: Learn how to insert data while maintaining relational integrity.
File I/O
2. **[Simple Query with Join](./assignment-2-simple-query-join/README.md)**  
   *Task*: Write a query to retrieve employee details along with their department name and location using joins.  
   *Goal*: Understand how to perform inner joins.

3. **[Salary Update with Trigger](./assignment-3-salary-update-trigger/README.md)**  
   *Task*: Create a trigger to automatically update an employee's salary based on department changes.  
   *Goal*: Learn how to use triggers to automate database operations.

4. **[Stored Procedure for Department Transfer](./assignment-4-department-transfer/README.md)**  
   *Task*: Write a stored procedure to transfer an employee to a new department, updating related details.  
   *Goal*: Practice writing and calling stored procedures.

5. **[Employee Promotion and Job Title Update](./assignment-5-promotion-job-title/README.md)**  
   *Task*: Promote employees based on their hire date, updating their job titles and salaries accordingly.  
   *Goal*: Work with conditional updates and joins.

6. **[Report Generation with Aggregates](./assignment-6-report-generation/README.md)**  
   *Task*: Generate a report that shows the number of employees per department and their average salary using aggregate functions.  
   *Goal*: Learn how to use `COUNT()`, `AVG()`, and `GROUP BY` to generate insights from data.

7. **[Employee Termination Trigger](./assignment-7-termination-trigger/README.md)**  
   *Task*: Create a trigger to handle employee terminations by logging their details into a separate table.  
   *Goal*: Automate record-keeping with triggers.

8. **[Query for Employee's Full Hierarchy](./assignment-8-hierarchy-query/README.md)**  
   *Task*: Write a query to find an employee’s manager and the manager’s department using self-joins.  
   *Goal*: Work with hierarchical data and self-joins.

9. **[Create View for Department Overview](./assignment-9-department-overview-view/README.md)**  
   *Task*: Create a view that summarizes each department’s total salary expenditure and number of employees.  
   *Goal*: Learn how to use views for easier querying.

10. **[Foreign Key Validation Procedure](./assignment-10-fk-validation-procedure/README.md)**  
    *Task*: Write a stored procedure that validates foreign key relationships before inserting new employees.  
    *Goal*: Ensure database integrity using stored procedures.

## How to Navigate the Assignments

Each assignment is located in its own folder and contains:
- A `README.md` file describing the task and goals in detail.
- An `.sql` file that includes the code required to solve the assignment.

Feel free to work through these assignments in any order, although we recommend starting from Assignment 1 for a progressive learning experience. Happy coding!
