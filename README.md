# CodingNomads-python-SQL-and-Databases-MySQL

## 1. Repository Contents 

1. [Repository Contents](#repository-contents)
2. [Outline](#2-outline)
3. [Files in This Repository](#3-files-in-this-repository)
   1. [databases Directory](#31-databases-directory)
   2. [course_notes Directory](#32-course_notes-directory)
   3. [course_automation_scripts Directory](#33-course_automation_scripts-directory)
      1. [Why I Automated My Work](#331-why-i-automated-my-work)
      2. [How I Automated My Work](#332-how-i-automated-my-work)
   4. [The course_automation_program.py file](#34-the-course_automation_programpy-file)
4. [To Clone This Repository](#4-to-clone-this-repository)

---

## 2. Outline

This repository contains my coursework for the CodingNomads [SQL & Databases course](https://codingnomads.com/course/learn-sql-mysql-databases). I completed this course as part of my independent learning to enhance my Python skills. This course was the third in CodingNomad’s ten-part [Python Web Development career track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp) series. This consisted of six core modules:

1. Introduction  
2. MySQL & MySQL Workbench  
3. Creating Relational Databases  
4. Importing MySQL Demo Database  
5. SQL Commands for Querying Databases  
6. Managing Databases  

This introduced Structured Query Language (SQL) as a language that interacts with Relational Database Management Systems (RDBMS). Multiple types of RDBMS applications were explored, showing a preference for MySQL Workbench. SQL was explored using the Sakila demonstration database, both in the terminal and with the MySQL Workbench GUI. The Sakila database contains information about actors, movies, and their rentals. MySQL Workbench was chosen for its open-source nature and ease of use relative to other RDBMS approaches. I learnt through completing this course that a relational database consists of multiple tables, which can be linked through primary and foreign keys. These keys have unique values to avoid data replication. Various methods of interacting with, backing up (dumping), and creating these databases were explored through SQL.

I primarily preferred interacting with MySQL in the terminal, rather than using MySQL Workbench. This first required running a MySQL installation, and then logging into it in the CLI. This required typing a password. Tutorials were then followed on the course webpage. These took the form of reading content, making notes while doing so, and then completing its instructions. Video notes were also completed, where appropriate.

This course was advertised with a 40-hour time completion, in comparison to the first two courses in the Python Web Development career track, which were advertised as 80 hours each. My repositories for the first two courses in this career track are [here](https://github.com/franpanteli/CodingNomads-python-101) and [here](https://github.com/franpanteli/CodingNomads-python-201). These courses were purely focused on Python, as opposed to the third course in its web development track, which covered SQL and databases.

After completing resources that covered the course content, I passed assessments to consolidate my knowledge. These consisted of thirteen quizzes and four journal entries. Journal entries for this covered foreign keys, query practice imports, and exports from MySQL. I pushed my course notes and files, wrote a project README.md file using PyCharm and the Grammarly text checker, and finally submitted a certificate of completion request on the CodingNomads platform to pass the course. The remainder of this README file provides a walkthrough of the files contained in my repository from completing the course.

---

## 3. Files in This Repository

### 3.1 databases Directory

The [databases directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/databases) in this repository was created through following the course content. Multiple examples containing databases were used in this course, primarily with the Sakila (films) database. Queries practicing on this database included operations on its actors table, creating functions (stored procedures) to operate on them, and limiting the number of returned results using the SQL `LIMIT` query. Multiple JOIN methods, such as `LEFT JOIN`, `RIGHT JOIN`, and `INNER JOIN` (default), were also explored.

---

### 3.2 course_notes Directory

The [course_notes directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/course_notes) contains my notes on course content. These notes were created in either webpage or Video Note format, depending on the mode in which the course content was presented. I wrote these notes in Python (.py) files, in line with the two previous Python courses I completed as part of the [career track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp). These were written with the PyCharm IDE, although this series of notes only contains text. These notes were spell-checked using the Grazie extension and are presented in chronological order. I found that the course took longer than 40 hours to complete (as advertised), due to making these in-depth notes.

---

### 3.3 course_automation_scripts Directory

#### 3.3.1 Why I Automated My Work

When working, I cloned a copy of my GitHub repository for the course on my Desktop. My workflow for course completion involved creating a new .py file where notes were to be taken and committing changes to GitHub whenever significant updates were made. These notes (contained in the [course_notes directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/course_notes)) were also named in a specific format. This involved naming them according to their number and titling the standard Python docstrings that each set of notes included. I found multiple issues with this, such as the tediousness of having to enter the same commands into the terminal to commit changes to GitHub. Since my course notes involved capitalisation to emphasise certain points, I also found that I sometimes typed lowercase text that I wanted capitalised. Rather than having to type the same text again in uppercase, I found it faster to write and use a Python program for this.

#### 3.3.2 How I Automated My Work

Although this was not included as part of the course material or suggestions, [this directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/course_automation_scripts) contains nine Python modules that I wrote and edited using ChatGPT to automate various tasks. When run, the [auto_git_push_scheduler.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/auto_git_push_scheduler.py) automatically pushes changes made to the course repository every minute. Below is a screenshot of this script when being left to run for three minutes without changes:

<div align="center">
  <img src="https://github.com/user-attachments/assets/a16af0c6-11b8-4dc1-98d8-7ba7a0cac777" alt="Auto Git Push Scheduler">
</div>

I leveraged this when writing notes, and found that the number of commits made while completing the course content was relatively higher compared to the previous two courses in the career track I had completed. The one-minute auto-push can be changed within its file. This module can be left running in the terminal; however, if only one commit is required, the [auto_git_push.py file](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/auto_git_push.py) can be run instead. An example output of this module is below, after attempting to commit no changes to the project:

<div align="center">
  <img src="https://github.com/user-attachments/assets/54163521-0553-4072-a74d-127830e37822" alt="Auto Git Push Example">
</div>

The [change_case.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/change_case.py) prompts the user to enter text, specifying whether it should be converted to uppercase or lowercase, and whether they want the text to be changed to uppercase or lowercase. I used this wherever I was writing notes, and I wanted text I had written in lowercase to be emphasised in uppercase - without having to rewrite it. An example of this is shown below:

<div align="center">
  <img src="https://github.com/user-attachments/assets/669f7708-02a1-42c2-bd3a-d60dace585bd" alt="Change Case Example">
</div>

The [clear_terminal.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/clear_terminal.py) is similar to a Bash clear command and clears the terminal. Next, the [create_notes.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/create_notes.py) generates .py files for writing course notes in. The .py files produced are created in the [course_notes directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/course_notes) and are automatically numbered. This module uses the `input()` function to ask users whether they would like to produce notes for a Webpage or a Video in the course, and names them accordingly. An example of this module output is shown below:

<div align="center">
  <img src="https://github.com/user-attachments/assets/3e158b27-c0ad-4991-b4cf-1487485f6b5f" alt="Create Notes Example">
</div>

The [delete_file.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/delete_file.py) can be used to delete a file in a given directory. The suggested method for doing this is to drag and drop the file from its directory into the terminal when prompted by the module’s user interface. The [open_file_in_pycharm.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/open_file_in_pycharm.py) can be used to open a file in PyCharm, and the [open_project_in_pycharm.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/open_project_in_pycharm.py) can be used to open the entire project repository in PyCharm. 

The [open_github_repo.py module](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_scripts/open_github_repo.py) can be used to launch a browser (specifically, Chrome) and open the URL for this project's repository. This module was used on several occasions to verify that the modules that auto-committed changes to project files were correctly functioning. This module utilises the Selenium WebDriver, which requires initial installation.  

---

### 3.4 The course_automation_program.py file

[This program](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/blob/main/course_automation_program.py) combines the Python modules located in the [course_automation_scripts directory](https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL/tree/main/course_automation_scripts) to create a user interface in the terminal for automating tasks related to course completion. A menu is first printed for the user, using the `input()` function. An image of this menu is shown below:

<div align="center">
  <img src="https://github.com/user-attachments/assets/4d4fbb47-3adc-4b14-9487-5d46e9338ea1" alt="Course Automation Program Menu">
</div>

This is contained within an infinite `while` loop, which repeatedly generates menu options after one has been selected and executed, unless the user selects to exit the program. A set of `if` blocks is used to import and execute the module relevant to the selected menu option. These modules were imported in statements, such as “from course_automation_scripts import auto_git_push_scheduler.” These were contained underneath each `if` block statement, rather than imported at the top of the code, to avoid automatically running them. It was not suggested that I write this program as a part of the course. I wrote this with ChatGPT and edited it using PyCharm to automate repetitive tasks during the process of creating course notes and other content.  

---

## 4. To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-SQL-and-Databases-MySQL.git
