""" Let's Add Some Data! Webpage Notes 
    -> this is a continuation of the previous SQL tutorial
    -> this was the same as opening MySQL in the terminal and typing in the SQL commands in the previous set of notes
    -> this is adding data to that database schema
    -> outline
        -> introduction
        -> how to insert data using MySQL Workbench
            -> select the database
            -> select a table and click the add data icon
            -> add values
            -> validate changes, by clicking "Apply"
            -> repeat this for each table
        -> summary: using 'MySQL Insert Into', to add data into a table
    -> we are adding data into the database
        -> this is manually using MySQL Workbench, or by using INSERT INTO SQL statements
            -> we are doing this without MySQL Workbench and in the terminal, because we already have this open
    -> we first select the database
        -> this is done with USE SocialDB;
    -> we then want to insert data into the user's table
        -> we can do this in MySQL Workbench, or achieve the same results using MySQL in the terminal
        -> this is done via
            INSERT INTO Users (FirstName, LastName, Email) VALUES
            ('Ed', 'Frinkel', 'ed@frinkel.co'),
            ('Sally', 'Doogooder', 'sally@doogooder.co'),
            ('George', 'Smith', 'george@smith.co');
            -> then checking it, using SELECT * FROM Users;
    -> then inserting data into the images table
        -> this is done with the SQL: 
"""