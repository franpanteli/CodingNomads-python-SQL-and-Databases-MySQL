""" ANY and or ALL Webpage Notes
    -> outline
        -> introduction
        -> What are SQL ANY and ALL Operators?
        -> How Does SQL ANY Work?
        -> How Does SQL ALL Work?
        -> SQL ANY / ALL Syntax
        -> SQL ANY / ALL Examples
            -> Using ANY with Numeric Columns
            -> Using ANY with Date Ranges
            -> Using ALL with Numeric Columns
            -> Using ALL with Subqueries
            -> Combining ANY / ALL with Other Conditions
        -> Advantages of ANY / ALL
        -> Common Pitfalls and Notes
        -> Best Practices
        -> Summary: SQL ANY and ALL Operators
    -> SQL ANY / ALL
        -> definition
            -> SQL ANY and SQL ALL are logical operators used inside the WHERE clause
            -> They allow you to compare a column's value against a **set of values returned by a subquery**
            -> ANY returns TRUE if the condition matches **any one of the values** in the subquery
            -> ALL returns TRUE if the condition matches **all of the values** in the subquery
            -> Both operators are often used with =, <, >, <=, >=, or <> operators
        -> usage context
            -> Filtering data using subqueries to dynamically generate comparison sets
            -> Performing advanced conditional queries
            -> Replacing complex OR conditions or multiple AND conditions with cleaner syntax
            -> Useful in analytics, reporting, and cross-table validations
        -> How Does SQL ANY Work?
            -> ANY tests a value against a set of values from a subquery
            -> Returns TRUE if the value meets the comparison condition with **at least one value** in the subquery
            -> Syntax example:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> = ANY (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
            -> Practical example:
                -> Get all customers who rented any film between May 25 and May 30, 2005:
                    SELECT first_name, last_name
                    FROM customer c
                    WHERE customer_id = ANY (
                        SELECT customer_id
                        FROM rental
                        WHERE rental_date BETWEEN '2005-05-25' AND '2005-05-30'
                    );
        -> How Does SQL ALL Work?
            -> ALL tests a value against a set of values from a subquery
            -> Returns TRUE only if the value meets the comparison condition with **every value** in the subquery
            -> Useful when you need to ensure a value satisfies all subquery results
            -> Syntax example:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> = ALL (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
            -> Practical example:
                -> Get all customers who rented on **all** of a specific date (e.g., May 25, 2005):
                    SELECT first_name, last_name
                    FROM customer c
                    WHERE customer_id = ALL (
                        SELECT customer_id
                        FROM rental
                        WHERE rental_date = '2005-05-25'
                    );
        -> SQL ANY / ALL Syntax
            -> ANY operator:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> <OPERATOR> ANY (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
            -> ALL operator:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> <OPERATOR> ALL (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
            -> Notes:
                -> <OPERATOR> can be =, >, <, >=, <=, <>, etc.
                -> Subquery must return one column
        -> SQL ANY / ALL Examples
            -> Using ANY with Numeric Columns
                -> Find products priced higher than **any** price in a discount table
                    SELECT product_name
                    FROM product
                    WHERE price > ANY (
                        SELECT discount_price
                        FROM discount
                    );
            -> Using ANY with Date Ranges
                -> Customers who rented any film within a date range:
                    SELECT first_name, last_name
                    FROM customer
                    WHERE customer_id = ANY (
                        SELECT customer_id
                        FROM rental
                        WHERE rental_date BETWEEN '2005-05-25' AND '2005-05-30'
                    );
            -> Using ALL with Numeric Columns
                -> Find products priced higher than **all** prices in a discount table
                    SELECT product_name
                    FROM product
                    WHERE price > ALL (
                        SELECT discount_price
                        FROM discount
                    );
            -> Using ALL with Subqueries
                -> Customers who rented **all films** on a specific date:
                    SELECT first_name, last_name
                    FROM customer
                    WHERE customer_id = ALL (
                        SELECT customer_id
                        FROM rental
                        WHERE rental_date = '2005-05-25'
                    );
            -> Combining ANY / ALL with Other Conditions
                -> Filter customers with rentals in a date range **and** a specific store:
                    SELECT first_name, last_name
                    FROM customer
                    WHERE customer_id = ANY (
                        SELECT customer_id
                        FROM rental
                        WHERE rental_date BETWEEN '2005-05-25' AND '2005-05-30'
                    )
                    AND store_id = 2;
        -> Advantages of ANY / ALL
            -> Simplifies complex subquery comparisons
            -> Reduces the need for multiple OR / AND conditions
            -> Can dynamically adapt to values returned from subqueries
            -> Powerful for cross-table validations and advanced analytics
        -> Common Pitfalls and Notes
            -> Subquery must return exactly **one column**
            -> ANY matches **one or more**, ALL requires **all matches**; misunderstanding this leads to errors
            -> Performance can be affected by large subquery result sets
            -> NULL values in subqueries can produce unexpected behavior; handle carefully
            -> Some databases support alternative syntax like IN with subqueries for ANY-like behavior
        -> Best Practices
            -> Use ANY when matching a value to a **subset** of potential values
            -> Use ALL when the value must satisfy **every item** in a subquery result
            -> Combine with AND / OR carefully for precise logic
            -> Consider indexes on subquery tables for performance optimization
            -> Avoid overly complex nested ANY / ALL queries that can reduce readability
        -> summary
            -> SQL ANY returns TRUE if a value matches **any** value from a subquery
            -> SQL ALL returns TRUE if a value matches **all** values from a subquery
            -> Both are used inside the WHERE clause
            -> Operators can be =, >, <, >=, <=, <>
            -> Essential for advanced filtering using subqueries and dynamic comparisons
            -> Syntax overview:
                -- ANY
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> <OPERATOR> ANY (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
                -- ALL
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> <OPERATOR> ALL (
                    SELECT <COLUMN>
                    FROM <OTHER_TABLE>
                    WHERE <CONDITION>
                );
"""