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
            INSERT INTO Posts (UserId, PostText, ImageId) VALUES
            (1, 'Ryan\'s First Post! Wahoo!', 4),
            (2, 'Kim\'s First Post! Yay!', 2),
            (3, 'Caden\'s First Post! Wow!', 3),
            (4, 'Martin\'s on social media? :)', 1);
        -> and checked with this: SELECT * FROM Posts;
        -> this allows us to PostID auto-increments
        -> Date defaults to the current timestamp
    -> then inserting data into the Users_Friends table
        -> we can connect friends, using this SQL:
            INSERT INTO Users_Friends (UserId_1, UserId_2) VALUES
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (3, 4);
        -> and check this worked using this: SELECT * FROM Users_Friends;
    -> we then verify the data with a Join
        -> this is done using this SQL:
            SELECT u.FirstName, u.LastName, p.PostText, i.ImageURL
            FROM Users u
            JOIN Posts p ON p.UserId = u.UserId
            JOIN Images i ON p.ImageId = i.ImageId
            WHERE u.UserId = 1;
        -> this shows Alice's (UserID 1) posts, with her associated images
        -> we can change u.UserId to 2 or 3 to see the other user's posts
    -> summary
        -> how to add rows to each table, using INSERT INTO in SQL
        -> how AUTO_INCREMENT and CURRENT_TIMESTAMP work automatically
        -> how to query joined data from multiple tables
    -> this is an SQL script that inserts all of this data into the database:
        USE SocialDB;

        -- Insert Users
        INSERT INTO Users (FirstName, LastName, Email) VALUES
        ('Ed', 'Frinkel', 'ed@frinkel.co'),
        ('Sally', 'Doogooder', 'sally@doogooder.co'),
        ('George', 'Smith', 'george@smith.co');

        -- Insert Images
        INSERT INTO Images (ImageURL) VALUES
        ('http://www.maravipost.com/wp-content/uploads/2017/07/computer-jokes-comic-book.jpg'),
        ('https://i.pinimg.com/originals/a1/15/9f/a1159f251ddca8438c2bbb0b0bf70eaa.png'),
        ('https://i.pinimg.com/originals/f2/3d/e2/f23de2ef2f598238e8f16bfb0c3c4cb5.jpg'),
        ('https://i.pinimg.com/originals/f8/d4/b3/f8d4b3b32c3c18b4972b97f6474655a8.jpg');

        -- Insert Posts
        INSERT INTO Posts (UserId, PostText, ImageId) VALUES
        (1, 'Ryan\'s First Post! Wahoo!', 4),
        (2, 'Kim\'s First Post! Yay!', 2),
        (3, 'Caden\'s First Post! Wow!', 3),
        (4, 'Martin\'s on social media? :)', 1);

        -- Insert Users_Friends relationships
        INSERT INTO Users_Friends (UserId_1, UserId_2) VALUES
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (3, 4);

        -- Verify the data
        SELECT * FROM Users;
        SELECT * FROM Images;
        SELECT * FROM Posts;
        SELECT * FROM Users_Friends;

        -- Example join query
        SELECT u.FirstName, u.LastName, p.PostText, i.ImageURL
        FROM Users u
        JOIN Posts p ON p.UserId = u.UserId
        JOIN Images i ON p.ImageId = i.ImageId
        WHERE u.UserId = 1;
"""