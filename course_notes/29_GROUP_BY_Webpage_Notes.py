""" GROUP BY Webpage Notes
    -> outline
        -> introduction
        -> How to Use GROUP BY in SQL
        -> SQL GROUP BY Examples
            -> Group By Actor
            -> Group By Customer
        -> Summary: SQL GROUP BY
    -> SQL GROUP BY
        -> definition
            -> GROUP BY is an SQL clause used to group rows that share a common value in one or more columns
            -> Often used with aggregate functions such as COUNT(), SUM(), AVG(), MAX(), MIN()
            -> Groups the result set so aggregate calculations can be applied per group
        -> usage context
            -> Useful for reporting, analytics, and summarizing data by categories or entities
            -> Allows you to determine totals, counts, or averages per group rather than across the entire table
            -> Typically comes after all JOINs and SELECTed tables, but before ORDER BY
    -> How to Use GROUP BY in SQL
        -> syntax
            -> SELECT <YOUR_COLUMNS>, AGG_FUNCTION(<COLUMN>) AS <NEW_COLUMN_NAME>
               FROM <YOUR_TABLE>
               [JOIN <OTHER_TABLES>]
               GROUP BY <COLUMN_TO_GROUP_BY>
               [ORDER BY <COLUMN_TO_SORT_BY>];
            -> <YOUR_COLUMNS>: non-aggregated columns you want to display
            -> AGG_FUNCTION: COUNT(), SUM(), AVG(), MAX(), MIN()
            -> <COLUMN_TO_GROUP_BY>: column(s) used to form groups
            -> ORDER BY optional: used to sort grouped results
        -> notes
            -> Every non-aggregated column in SELECT must appear in GROUP BY
            -> Can group by multiple columns if needed: GROUP BY column1, column2
            -> Typically combined with JOINs to aggregate across related tables
    -> SQL GROUP BY Examples
        -> Group By Actor
            -> scenario
                -> Determine total number of films each actor has acted in
            -> query
                SELECT a.first_name, a.last_name, COUNT(a.actor_id) AS num_films
                FROM actor a
                JOIN film_actor fa ON a.actor_id = fa.actor_id
                JOIN film f ON fa.film_id = f.film_id
                GROUP BY a.actor_id
                ORDER BY num_films DESC;
            -> notes
                -> Uses COUNT() to calculate number of films per actor
                -> GROUP BY a.actor_id ensures aggregation happens per actor
                -> ORDER BY num_films DESC lists actors from most to least films
        -> Group By Customer
            -> scenario
                -> Determine total payments per customer to find best customers
            -> query
                SELECT c.first_name, c.last_name, SUM(p.amount) AS total_payments
                FROM customer c
                JOIN payment p ON c.customer_id = p.customer_id
                GROUP BY c.customer_id
                ORDER BY total_payments DESC;
            -> notes
                -> Uses SUM() to total payments per customer
                -> GROUP BY c.customer_id ensures aggregation per customer
                -> ORDER BY total_payments DESC sorts customers from highest to lowest payments
    -> summary
        -> GROUP BY groups rows in the result set by one or more columns
        -> Commonly used with aggregate functions (COUNT, SUM, AVG, MAX, MIN)
        -> Syntax order: SELECT → FROM → [JOIN] → GROUP BY → [ORDER BY]
        -> Non-aggregated SELECT columns must appear in GROUP BY
        -> Can combine GROUP BY with WHERE for filtered aggregation
        -> Can combine GROUP BY with ORDER BY to sort aggregated results
        -> Essential for reporting and summarizing data per entity or category
"""