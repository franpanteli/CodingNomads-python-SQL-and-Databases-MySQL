""" IN Webpage Notes
    -> outline
        -> introduction
        -> How Does the SQL IN Statement Work?
        -> SQL IN Syntax
        -> SQL IN Examples
            -> Basic Example
            -> Using IN with Strings
            -> Using IN with Subqueries
            -> Using IN with NOT IN
        -> Advantages of SQL IN
        -> Summary: SQL IN Statement
    -> SQL IN
        -> definition
            -> SQL IN is a logical operator used in the WHERE clause to filter rows that match any value in a list
            -> Functionally equivalent to multiple OR conditions but cleaner and easier to maintain
            -> Works with numeric, string, and date columns
            -> Can be combined with aggregate functions, JOINs, and other conditions
        -> usage context
            -> Filter datasets to match multiple known values
            -> Replace repetitive OR statements in queries
            -> Often used in reporting, analytics, and data validation
        -> How Does the SQL IN Statement Work?
            -> Evaluates whether a column's value exists in a given list of values
            -> Returns TRUE if any value in the list matches the column
            -> Equivalent query using OR:
                SELECT <columns>
                FROM <table>
                WHERE <column> = <value1>
                   OR <column> = <value2>
                   OR <column> = <value3>;
            -> Placing IN inside WHERE allows for cleaner, readable queries especially with many values
        -> SQL IN Syntax
            -> Basic syntax:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> IN (<VALUE_1>, <VALUE_2>, <VALUE_3>, ...);
            -> Components:
                -> <YOUR_COLUMNS>: columns to retrieve
                -> <YOUR_TABLE>: table to query
                -> <YOUR_COLUMN>: column being filtered
                -> <VALUE_1>, <VALUE_2>, ... : values to match against
        -> SQL IN Examples
            -> Basic Example
                -> Select films released in 2004, 2005, or 2006
                    SELECT * FROM film
                    WHERE release_year IN (2004, 2005, 2006);
            -> Using IN with Strings
                -> Select customers from specific cities
                    SELECT first_name, last_name
                    FROM customer
                    WHERE city IN ('London', 'Paris', 'Tokyo');
            -> Using IN with Subqueries
                -> Filter films by actors who appear in a specific category
                    SELECT title
                    FROM film
                    WHERE film_id IN (
                        SELECT film_id
                        FROM film_actor
                        WHERE actor_id IN (1, 2, 3)
                    );
            -> Using IN with NOT IN
                -> Exclude certain values from results
                    SELECT title
                    FROM film
                    WHERE release_year NOT IN (2001, 2002, 2003);
        -> Advantages of SQL IN
            -> Simplifies queries compared to multiple OR statements
            -> Easier to read and maintain, especially with long lists
            -> Supports subqueries to dynamically generate lists of values
            -> Can be combined with NOT IN for exclusion filters
            -> Reduces query complexity while keeping logic clear
        -> notes & best practices
            -> NULL values in IN list can produce unexpected results; be careful when using NOT IN with NULLs
            -> Large lists of static values are okay, but for very large lists, using JOINs or subqueries may be more efficient
            -> Works best for discrete sets of values, not ranges (use BETWEEN for ranges)
            -> Can be combined with LIKE, GROUP BY, ORDER BY, and aggregate functions for advanced reporting
        -> summary
            -> SQL IN filters a column to match any value from a list
            -> Equivalent to multiple OR conditions but cleaner
            -> Can contain numeric, string, or date values
            -> Supports subqueries and NOT IN for dynamic filtering
            -> Essential for querying subsets of data efficiently
            -> Syntax overview:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> IN (<VALUE_1>, <VALUE_2>, ...);
"""