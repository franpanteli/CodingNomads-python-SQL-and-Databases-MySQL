""" DELETE Webpage Notes
    -> outline
        -> introduction
        -> how does DELETE work?
        -> DELETE statement examples
            -> 1. safe way to delete data
            -> 2. dangerous way to delete data
        -> summary: DELETE statement
    -> TO REMOVE DATA FROM THE DATABASE
    -> choose the table that contains the data
    -> WE APPLY A BOOLEAN CONDITION TO SPECIFY WHAT DATA WE WANT TO REMOVE
    -> examples
        -> 1. safe way to delete data
            -> DELETE FROM sakila.actor
            -> WHERE actor_id = 201;
                -> IT'S SAFER TO APPLY A SPECIFIC WHERE CONDITION WHEN DELETING DATA FROM THE DATABASE
                -> WE CAN TELL IF THIS HAS WORKED OR NOT, BY LOOKING AT THE NUMBER OF ROWS UNDER "RESPONSE" IN MYSQL
                    WORKBENCH
                -> this tells you the amount of time the query took to run
        -> 2. dangerous way to delete data
            delete from actor; -- bad (do not run this)
            -> YOU NEED TO USE A WHERE STATEMENT WHEN DELETING THE DATA
                -> THIS IS SAFER
            -> WITHOUT USING A WHERE CLAUSE, ALL RECORDS WILL BE DELETED FROM THE TABLE
            -> THERE IS NO UNDO FOR THIS IN THE TABLE
            -> COMMENTS ARE MADE WITH -- ON THE END OF THE SQL STATEMENT LINE
    -> summary
        -> DELETE <- this deletes data from the database
            -> IF YOU DON'T USE A WHERE QUERY, THEN ALL OF THE INFORMATION IN THE DATABASE WILL BE DELETED, WITHOUT
                RECOURSE OR REVERSABILITY
        -> DELETE syntax:
            -> DELETE FROM <YOUR_TABLE>
            -> WHERE <YOUR_CONDITION>;
                -> our data is inserted in the <> brackets
    -> next <- video on how to update and delete information from the database table
"""