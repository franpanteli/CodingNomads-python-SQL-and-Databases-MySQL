""" INNER JOIN Webpage Notes 
    -> outline
        -> introduction
        -> what is INNER JOIN?
        -> INNER JOI example
            -> 1. select your tables to join
            -> 2. select the join columns
            -> 3. optional: add a conditional statement
            -> 4. run the query
        -> INNER JOIN example - explained
            -> INNER JOIN tips
        -> summary: the INNER JOIN statement
    -> INNER JOIN
        -> joining one or more tables together
        -> INNER JOIN IS THE DEFAULT JOIN IN MYSQL
        -> INNER JOIN SELECTS ALL RECORDS THAT HAVE MATCHING VALUES IN THE **TWO** CHOSEN TABLES
    -> INNER JOIN example
        -> 1. select your tables to join
            -> CHOOSE THE TWO TABLES WE WANT TO JOIN
            -> joining the `actor`, `film_actor` and `film` tables

        -> 2. select the join columns
            -> JOINING TABLES USING THEIR COLUMNS
            -> THERE HAVE TO BE CORRESPONDING COLUMNS THAT HAVE CORRESPONDING VALUES
                -> WE WANT TO JOIN THE TWO TABLES BY THESE VALUES
            -> for example, the two tables we want to join contain the same ID's
                -> we want to join them by this column

        -> 3. optional: add a conditional statement
            -> we can filter the results with a condition instead of getting more information than we need
            -> this is done, by using the WHERE statement
            -> selecting all films that a certain actor is in, for example

        -> 4. run the query
            SELECT actor.first_name, actor.last_name, film.title, film.release_year -- fields to select
            FROM actor   --first table to select from
            INNER JOIN film_actor  -- first table to join
                ON actor.actor_id = film_actor.actor_id  -- the field on which to join the two tables
            INNER JOIN film -- second table to join
                ON film_actor.film_id = film.film_id -- the field on which to join the two tables
            WHERE actor.first_name = "PENELOPE" AND actor.last_name = "GUINESS"; -- boolean condition to filter results


    -> INNER JOIN example - explained
    -> INNER JOIN tips
    -> summary: the INNER JOIN statement
"""