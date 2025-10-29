""" CREATE TABLE SELECT Webpage Notes 
    -> outline
        -> introduction
        -> how to create a table in SQL
        -> examples of the CREATE TABLE SELECT statement
            -> 1. CREATE TABLE, SELECT ALL
            -> 2. CREATE TABLE, select specific columns
        -> summary: the SQL CREATE TABLE query
    -> CREATE TABLE <- TO CREATE A TABLE, BASED ON THE RESULTS OF A SELECT QUERY
    -> this defines the order of the command
    -> we CREATE TABLE and choose its name, then selecting what you would like in another table
    -> examples
        -> 1. CREATE TABLE, SELECT ALL
            -> using the `film` and `actor` table in the sakila database
            -> CREATE TABLE actor_backup SELECT * FROM actor;
                -> MAKING A BACKUP OF THE ACTOR TABLE
                -> creating a ctable called actor_backup
                -> selecting everything from the actors table
                -> we are selecting everything from the actors table and creating another table from this
            -> WE THEN REFRESH THE SCHEMA NAVIGATOR ON THE LEFT
                -> this runs a refresh
                -> spinning arrows icon
            -> TO BACKUP THE TABLE, YOU NEED TO CREATE A BLANK TABLE, WHICH THE INFORMATION FROM ANOTHER ONE IS THEN
                COPIED INTO
                -> this is done by selecting all the rows in a table and coppying them over
        -> 2. CREATE TABLE, SELECT SPECIFIC COLUMNS
            -> YOU DON'T NEED TO USE *, YOU CAN WRITE THE NAMES OF THE TABLES YOU WANT TO COPPY INSTEAD

            CREATE TABLE kids_movies
            SELECT title, length, rating
            FROM film
            WHERE rating = "G"
            AND length < 60
                -> THIS IS USED FOR CREATING LOOKUP TABLES, AS WELL AS FOR CREATING BACKUPS OF TABLES
                    -> these can later be deleted, or re-backed up when the data changes
                -> this is useful if we are doing something potentially risky and want a table backup
                -> this can be used with JOIN statements

            DROP TABLE sakila.kids_movies;
            DROP TABLE sakila.actor_backup;
                -> dropping the new tables we created, to keep the database tidy
    -> summary
        -> 
"""