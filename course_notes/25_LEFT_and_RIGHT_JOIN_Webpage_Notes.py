""" LEFT and RIGHT JOIN Webpage Notes 
    -> outline
        -> introduction
        -> what is LEFT JOIN?
        -> what is RIGHT JOIN?
        -> LEFT JOIN vs RIGHT JOIN
        -> example of LEFT JOIN vs RIGHT JOIN
            -> LEFT JOIN example
            -> RIGHT JOIN example
            -> RIGHT / LEFT JOIN vs INNER JOIN
        -> summary: LEFT JOIN and RIGHT JOIN
    -> INNER JOIN returns all results where there is a matching record in each table
    -> SOMETIMES, YOU NEED ALL THE RECORDS FROM ONE TABLE WHETHER OR NOT THERE IS A MATCHING RECORD IN THE JOIN TABLE
        -> this is where a LEFT or RIGHT JOIN is used
    -> LEFT JOIN
        -> THIS RETURNS ALL ROWS FROM THE LEFT TABLE (THE FIRST TABLE IN THE JOIN CLAUSE)
        -> this happens even if there is no matching record in the right table
    -> RIGHT JOIN
        -> this returns all the rows from the right table
            -> THE RIGHT TABLE IS THE SECOND ONE MENTIONED IN THE JOIN CLAUSE
    -> LEFT JOIN vs RIGHT JOIN
        -> LEFT IS THE FIRST TABLE IN THE QUERY, RIGHT IS THE SECOND TABLE IN THE QUERY
            -> this is whether or not there are matches in the other table
    -> example of LEFT JOIN vs RIGHT JOIN
        -> about
            -> getting a list of customers, from the `customers` table
            -> if we also want to return a list of actors, from the `actors` table
            -> we want these ones that share a first / last name with the customer
            -> this requires the entire list of customers
                -> we want to include data that isn't unique
            -> a LEFT JOIN can be used for this
                -> to get all records ƒrom the `customer` table, as well as any matching records from the `actor` table
                -> WHEN THERE IS NO MATCH WITH A JOIN QUERY, A NULL RESULT IS RETURNED
                    -> THERE IS A CASE WHERE THE ENTIRE QUERY RETURNS NULL VALUES N THE ROW
        -> LEFT JOIN example
            SELECT
                c.first_name,
                c.last_name,
                a.first_name,
                a.last_name
                -> we are selecting all of these columns
            FROM customer c
                -> CREATING AN ALIAS FOR THE CUSTOMERS TABLE (C)
            LEFT JOIN actor a
                -> EXECUTING A LEFT JOIN, AND IMPLEMENTING AN ALIAS FOR THE ACTORS TABLE (A)
                -> THIS IS A LETTER AT THE END OF THE QUERY LINE
            ON c.last_name = a.last_name
            ORDER BY c.last_name;
                -> ordering the results from this, according to the data in the `last_name` column
                -> A LEFT JOIN SELECTS ALL RECORDS FROM THE LEFT (FIRST MENTIONED) TABLE, AND ONLY THE RESULTS FROM THE
                    SECOND (RIGHT) TABLE, IF THEY ARE MATCHING
                        -> BOOLEAN STATEMENTS CAN BE USED FOR THIS
                        -> THIS IS LIKE STANDARD GATES IN COMPUTER SCIENCE
                -> IF THEY DON'T MATCH, IT SHOWS NULL
                    -> in this case, it's in the second (rightmost) table, because we are using a LEFT  (first mentioned
                        table) JOIN
        -> RIGHT JOIN example
            SELECT
                c.first_name,
                c.last_name,
                a.first_name,
                a.last_name
                -> selecting the columns from the database
            FROM customer c
                -> SETTING UP AN ALIAS FOR THE CUSTOMERS TABLE
            RIGHT JOIN actor a
                -> EXECUTING A RIGHT JOIN FO RIGHT TABLE WITH THE ACTORS TABLE, AND GIVING THIS AN ALIAS OF A
            ON c.last_name = a.last_name
            -> we read the `customer` table, before we read the `actor` table
            -> RIGHT JOINs are the opposite of LEFT JOINs
            -> IT SHOWS NULL IF THERE IS NO MATCH
        -> RIGHT / LEFT JOIN vs INNER JOIN
            SELECT
                c.first_name,
                c.last_name,
                a.first_name,
                a.last_name
                -> return the column names
            FROM customer c
                -> use an alias of c for the `customer` table
            INNER JOIN actor a
                -> execute an INNER JOIN (default) with the actors table, with an alias of a
            ON c.last_name = a.last_name
                -> execute the JOIN on these two columns
            -> AN INNER JOIN IS ONLY USED IF WE WANT THE DATA FROM BOTH TABLES THAT MATCH
            -> IT IS LIKE THE OVERLAP OF TWO SETS OF DATA (TWO COLUMNS / TABLES)
                -> (per each entry)
            -> YOU DON'T HAVE TO TPE INNER JOIN, BECAUSE IT'S DEFAULT
            -> this can be done in MySQL Workbench (the GUI application), or in the terminal
    -> summary: LEFT JOIN and RIGHT JOIN
        -> LEFT / RIGHT JOINs
            -> LEFT JOIN AND RIGHT JOIN ARE USED TO SELECT ALL RESULTS FROM ONE TABLE, AND ONLY THE MATCHING RESULTS FROM
                THE OTHER
            -> LEFT JOIN TAKES ALL RESULTS FROM THE LEFT (FIRST) TABLE, AND ONLY MATCHING RESULTS FROM THE SECOND (RIGHT)
                TABLE. ALL OTHER NON-MATCHING VALUES ARE NULL IN THE RIGHTMOST TABLE
                -> RIGHT JOIN is the opposite, with the second table representing the right one
            -> LEFT and RIGHT are synonymous with first and second tables written in the query
        -> LEFT JOIN / RIGHT JOIN syntax
            SELECT <YOUR_COLUMNS>
                -> we select the columns in the first (left table)
            FROM <YOUR_TABLE_1>
                -> to create an alias (see examples for customers / actors table aliases above)
            <LEFT_or_RIGHT> JOIN <YOUR_TABLE_2>
            ON <YOUR_TABLE_1.COLUMN> = <YOUR_TABLE_2.COLUMN>
            -> we place our data inside the <> symbols
            -> THIS MEANS 'JOIN THE TWO TABLES'
        -> wa
"""