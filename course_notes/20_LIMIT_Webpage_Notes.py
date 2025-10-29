""" LIMIT Webpage Notes 
    -> outline
        -> introduction
        -> how does SQL LIMIT work?
        -> SQL LIMIT examples
            -> 1. Limit 10 from 1 table
            -> 2. Limit 5 from 2 tables
        -> avoid this error with SQL limit
        -> summary: SQL LIMIT query
    -> this is a utility statement
    -> THIS LIMITS THE NUMBER OF RESULTS WE WILL GET BACK
    -> WE PLACE THIS AT THE END OF THE QUERY
    -> LIMIT examples
        -> LIMIT 10 1 from Table
            -> we are using customer and payment tables
            -> SELECT * FROM customer
            -> LIMIT 10;
            -> selecting everything from the customer table
            -> THEN LIMITING THE RESPONSES TO 10
        -> LIMIT 5 from 2 tables
            -> a GROUP BY example, where we limit the total number of payments for all customers
            -> limiting this to 5 results, for the 5 best customers
            -> SQL:
                -> SELECT c.first_name, c.last_name, SUM(p.amount) as total_payments
                    -> selecting different columns: first name, last name and the total number of money the customer has
                        spent
                -> FROM customer c
                    -> running other SQL statements
                -> JOIN payment p
                -> ON c.customer_id = p.customer_id
                -> GROUP BY c.customer_id
                -> ORDER BY total_payments DESC
                -> LIMIT 5;
                    -> LIMITING THE TOTAL NUMBER OF RESULTS TO 5
    -> avoid this error with LIMIT

SELECT c.first_name, c.last_name, SUM(p.amount) as total_payments
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id
LIMIT 5
ORDER BY total_payments DESC;


    -> summary
"""