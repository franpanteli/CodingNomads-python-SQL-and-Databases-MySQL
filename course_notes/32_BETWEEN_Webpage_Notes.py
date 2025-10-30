""" BETWEEN Webpage Notes
    -> outline
        -> introduction
        -> How Does SQL BETWEEN Work?
        -> SQL BETWEEN Statement Syntax
        -> SQL BETWEEN Examples
            -> Numeric Range Example
            -> Date Range Example
            -> Chaining Multiple Conditions
            -> Equivalence with AND
        -> Advantages of SQL BETWEEN
        -> Notes & Best Practices
        -> Summary: SQL BETWEEN Statement
    -> SQL BETWEEN
        -> definition
            -> The SQL BETWEEN operator is used in the WHERE clause to filter rows based on a range of values
            -> Returns all rows where the column value is **greater than or equal to** the lower bound and **less than or equal to** the upper bound
            -> Works with numeric, date, and sometimes string columns depending on the database
            -> Functionally similar to an AND expression (column >= value1 AND column <= value2)
        -> usage context
            -> Filtering data within a specific numeric, date, or string range
            -> Simplifies queries that would otherwise require multiple AND conditions
            -> Useful for reporting, analytics, and time-based queries
        -> SQL BETWEEN Statement Syntax
            -> Basic syntax:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> BETWEEN <VALUE_1> AND <VALUE_2>;
            -> Components:
                -> <YOUR_COLUMNS>: Columns to select
                -> <YOUR_TABLE>: Table to query
                -> <YOUR_COLUMN>: Column to filter
                -> <VALUE_1> AND <VALUE_2>: Lower and upper bounds of the range
        -> SQL BETWEEN Examples
            -> Numeric Range Example
                -> Count payments with amounts between $3 and $5
                    SELECT COUNT(payment_id) AS num_payments
                    FROM payment
                    WHERE amount BETWEEN 3 AND 5;
            -> Equivalence with AND
                -> Same query using AND instead of BETWEEN
                    SELECT COUNT(payment_id) AS num_payments
                    FROM payment
                    WHERE amount >= 3 AND amount <= 5;
            -> Date Range Example
                -> Select payments made in January 2005
                    SELECT *
                    FROM payment
                    WHERE payment_date BETWEEN '2005-01-01' AND '2005-01-31';
            -> Chaining Multiple Conditions
                -> Technically possible but rarely needed; BETWEEN is designed for two values
                -> Example (not common): WHERE amount BETWEEN 3 AND 5 AND other_column BETWEEN 10 AND 20
        -> Advantages of SQL BETWEEN
            -> Simplifies range queries
            -> Makes queries more readable compared to multiple AND conditions
            -> Works for numeric, date, and sometimes string ranges
            -> Reduces query complexity while maintaining clarity
        -> Notes & Best Practices
            -> BETWEEN is inclusive of both endpoints (>= lower bound AND <= upper bound)
            -> Be careful with date and time formats; ensure correct formatting to avoid missing rows
            -> For exclusive ranges, combine > and < operators instead of BETWEEN
            -> Can be combined with other conditions (AND, OR, LIKE) for more advanced filtering
            -> Avoid chaining too many BETWEEN conditions; use multiple columns or JOINs instead
        -> summary
            -> SQL BETWEEN filters rows by a range of values in a column
            -> Equivalent to using AND for the lower and upper bounds
            -> Syntax overview:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> BETWEEN <VALUE_1> AND <VALUE_2>;
            -> Works for numeric, date, and some string columns
            -> Essential for range-based queries in reporting, analytics, and data validation
"""