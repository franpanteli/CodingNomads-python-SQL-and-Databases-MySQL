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
            INSERT INTO Images (ImageURL) VALUES
            ('http://www.maravipost.com/wp-content/uploads/2017/07/computer-jokes-comic-book.jpg'),
            ('https://i.pinimg.com/originals/a1/15/9f/a1159f251ddca8438c2bbb0b0bf70eaa.png'),
            ('https://i.pinimg.com/originals/f2/3d/e2/f23de2ef2f598238e8f16bfb0c3c4cb5.jpg'),
            ('https://i.pinimg.com/originals/f8/d4/b3/f8d4b3b32c3c18b4972b97f6474655a8.jpg');
        -> and checked with: SELECT * FROM Images;
    -> we then insert data into the posts table
        -> this can be done with this SQL: 
"""