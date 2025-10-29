""" ORDER BY Webpage Notes 
    -> outline
        -> introduction
        -> how does SQL ORDER BY work?
        -> SQL ORDER BY examples
            -> 1. SQL ORDER BY ascending
            -> 2. SQL ORDER BY descending
            -> 3. SQL ORDER BY field
        -> Summary: SQL ORDER BY
    -> ORDER BY
        -> this is a utility keyword
        -> elements
            -> the SELECT statement can be followed with ORDER BY
            -> one or multiple columns can be ordered
            -> we can choose the order type we want
        -> examples
            -> order by ascending
                -> SELECT * from actor
                    -> selecting all actors
                -> ORDER BY first_name ASC;
                    -> ordering †hem by first name in ascending order
                -> we can use DESC for descending
            -> order by descending
                -> SELECT * from actor
                    -> selecting everything from the actors table
                -> ORDER BY last_name DESC;
                    -> ordering this by last name in descending order
            -> order by field
                -> SELECT * from actor
                -> ORDER BY actor_id;
                    -> A FIELD IS SOMETHING GENERAL, LIKE THE ID OF THE ACTORS
                    -> THIS CAN BE USED TO ORDER THE ACTORS BY
                    -> we are selecting everything from the table
                    -> we are then ordering this by the data in the actor_id column
        -> summary
            -> ORDER BY ORDERS THE ROWS of the table
                -> ASC <- ASCENDING ORDER (DEFAULT)
                -> DEC <- DESCENDING ORDER
            -> THIS COMES AFTER A SELECT QUERY
            -> general syntax:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                ORDER BY <YOUR_COLUMNS> ASC
        -> LIMIT <- next; to select some of the rows that we want the query to return 
"""