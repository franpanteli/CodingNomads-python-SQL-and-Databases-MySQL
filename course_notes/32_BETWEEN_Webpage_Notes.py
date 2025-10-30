""" BETWEEN Webpage Notes
    -> outline
        -> introduction
        -> What is SQL BETWEEN?
        -> How Does SQL BETWEEN Work?
        -> SQL BETWEEN Statement Syntax
        -> SQL BETWEEN Examples
            -> Numeric Range Example
            -> Date Range Example
            -> String Range Example
            -> Equivalence with AND
            -> Using Multiple Columns
        -> Advantages of SQL BETWEEN
        -> Common Pitfalls and Notes
        -> Best Practices
        -> Summary: SQL BETWEEN Statement
    -> SQL BETWEEN
        -> definition
            -> The SQL BETWEEN operator filters rows in a result set based on a range of values
            -> Includes **both endpoints**: BETWEEN is inclusive of lower and upper bounds
            -> Works for numeric, date/time, and sometimes string columns
            -> Simplifies queries compared to writing multiple AND conditions
        -> usage context
            -> Filtering data within a numeric, date, or string range
            -> Reporting and analytics queries
            -> Time-based queries, e.g., filtering by years, months, or specific date ranges
            -> Range-based validation in database management
        -> How Does SQL BETWEEN Work?
            -> Evaluates whether a column value falls between two specified values
            -> Returns TRUE if the column value is **>= lower bound AND <= upper bound**
            -> Example logic:
                column_value BETWEEN value1 AND value2
                is equivalent to:
                column_value >= value1 AND column_value <= value2
        -> SQL BETWEEN Statement Syntax
            -> Basic syntax:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> BETWEEN <VALUE_1> AND <VALUE_2>;
            -> Components:
                -> <YOUR_COLUMNS>: Columns to retrieve
                -> <YOUR_TABLE>: Table to query
                -> <YOUR_COLUMN>: Column being filtered
                -> <VALUE_1> AND <VALUE_2>: Lower and upper bounds of the range
            -> Notes:
                -> BETWEEN is inclusive; to exclude endpoints, use > and < operators
                -> Can be combined with other WHERE conditions using AND/OR
        -> SQL BETWEEN Examples
            -> Numeric Range Example
                -> Count payments with amounts between $3 and $5
                    SELECT COUNT(payment_id) AS num_payments
                    FROM payment
                    WHERE amount BETWEEN 3 AND 5;
            -> Equivalence with AND
                -> Same query using AND:
                    SELECT COUNT(payment_id) AS num_payments
                    FROM payment
                    WHERE amount >= 3 AND amount <= 5;
            -> Date Range Example
                -> Select payments made in January 2005
                    SELECT *
                    FROM payment
                    WHERE payment_date BETWEEN '2005-01-01' AND '2005-01-31';
            -> String Range Example
                -> Select films whose titles fall alphabetically between 'A' and 'F'
                    SELECT title
                    FROM film
                    WHERE title BETWEEN 'A' AND 'F';
            -> Using Multiple Columns
                -> Filter using multiple BETWEEN conditions on different columns
                    SELECT *
                    FROM payment
                    WHERE amount BETWEEN 3 AND 5
                      AND payment_date BETWEEN '2005-01-01' AND '2005-12-31';
        -> Advantages of SQL BETWEEN
            -> Reduces query complexity compared to multiple AND conditions
            -> Improves readability and maintainability
            -> Works with numeric, date, and some string ranges
            -> Inclusive behavior ensures no records are accidentally excluded
            -> Efficient for database engines to process compared to multiple OR/AND comparisons
        -> Common Pitfalls and Notes
            -> BETWEEN is inclusive; be careful if you want exclusive ranges
            -> Ensure correct data type matching; e.g., string vs numeric vs date
            -> In some databases, string ranges depend on collation and case sensitivity
            -> Using NOT BETWEEN excludes all values within the range
            -> Avoid using BETWEEN with NULL values; it returns FALSE if the column is NULL
        -> Best Practices
            -> Use BETWEEN for clear, inclusive range filtering
            -> For exclusive ranges, prefer > and < operators
            -> Combine with AND/OR and other filters for advanced queries
            -> Ensure proper data formatting for dates and strings
            -> Avoid chaining multiple BETWEEN conditions unnecessarily; use multiple WHERE clauses instead
        -> summary
            -> SQL BETWEEN filters rows by a **range of values**
            -> Equivalent to column >= value1 AND column <= value2
            -> Inclusive of both endpoints
            -> Works for numeric, date, and some string columns
            -> Syntax overview:
                SELECT <YOUR_COLUMNS>
                FROM <YOUR_TABLE>
                WHERE <YOUR_COLUMN> BETWEEN <VALUE_1> AND <VALUE_2>;
            -> Essential for range-based queries in reporting, analytics, and validations
"""