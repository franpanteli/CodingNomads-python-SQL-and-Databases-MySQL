""" AND, OR, NOT Webpage Notes 
    -> outline
        -> introduction
        -> what is the SQL AND operator?
            -> SQL AND operator example
        -> What is teh SQL OR statement?
            -> SQL OR statement example
        -> What is the SQL NOT query?
            -> SQL NOT operator example
        -> Summary: SQL AND, SQL OR, and SQL NOT queries
    -> AND
        -> THIS RETURNS TRUE IF BOTH RESULTS ARE TRUE
        -> SELECT * FROM film WHERE length < 50 AND rating = "G"; <- to look for a movie rated G
            -> the length of the film is < 50 and the rating is G
        -> this can be run in MySQL Workbench (GUI), or in the terminal
    -> OR
        -> IF AT LEAST ONE OF THE STATEMENTS IS TRUE
        -> SELECT * FROM sakila.film where rating = "G" OR rating = "PG";
            _> selecting all of the film data, where the rating is G or PG (both of those conditions are True)
            -> this returns a lot more results than the AND query does, because there are more True statements on either
                side than there are on both
    -> OR and AND together
        -> SELECT * FROM sakila.film where rating = "G" OR rating = "PG" OR rating = "PG-13";
        -> this uses three OR statements 
"""