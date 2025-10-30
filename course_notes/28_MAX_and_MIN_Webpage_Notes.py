""" MAX and MIN Webpage Notes
    -> outline
        -> introduction
        -> SQL MAX Function
            -> purpose
            -> syntax
            -> examples
            -> notes & best practices
        -> SQL MIN Function
            -> purpose
            -> syntax
            -> examples
            -> notes & best practices
        -> Summary: SQL MAX & SQL MIN
    -> SQL MAX / MIN
        -> definition
            -> MAX() and MIN() are aggregate functions in SQL
            -> MAX() returns the largest value in a column
            -> MIN() returns the smallest value in a column
            -> These functions can operate on numeric and date/time (DATETIME) columns
            -> Aggregate functions summarize data across multiple rows
        -> usage context
            -> Identify extreme values in datasets (highest payment, earliest date, max score)
            -> Useful in analytics, reporting, and decision-making queries
            -> Often combined with WHERE clauses, GROUP BY, or ORDER BY for more precise analysis
    -> SQL MAX Function
        -> purpose
            -> To determine the maximum value of a column in a table
            -> Helps identify top-performing records or the latest dates
        -> syntax
            -> SELECT MAX(<COLUMN_NAME>) AS <NEW_COLUMN_NAME>
               FROM <TABLE_NAME>;
            -> <COLUMN_NAME>: the column to analyze (numeric or date/time)
            -> AS <NEW_COLUMN_NAME>: optional, renames the result column for clarity
        -> examples
            -> Example 1: Find the largest payment in the payment table
                SELECT MAX(amount) AS largest_payment
                FROM payment;
            -> Example 2: Find the latest payment date
                SELECT MAX(payment_date) AS latest_payment
                FROM payment;
            -> Example 3: Using MAX with a WHERE condition
                SELECT MAX(amount) AS max_payment_2005
                FROM payment
                WHERE payment_date >= '2005-01-01'
                  AND payment_date < '2006-01-01';
        -> notes & best practices
            -> MAX() ignores NULL values in the column
            -> Often used with GROUP BY to find the maximum per category
                Example:
                SELECT customer_id, MAX(amount) AS max_payment
                FROM payment
                GROUP BY customer_id;
            -> Can be combined with ORDER BY to highlight top results
    -> SQL MIN Function
        -> purpose
            -> To determine the minimum value of a column in a table
            -> Helps identify lowest values, earliest dates, or minimum scores
        -> syntax
            -> SELECT MIN(<COLUMN_NAME>) AS <NEW_COLUMN_NAME>
               FROM <TABLE_NAME>;
            -> <COLUMN_NAME>: numeric or date/time column
            -> AS <NEW_COLUMN_NAME>: optional, renames the result column
        -> examples
            -> Example 1: Find the smallest payment in the payment table
                SELECT MIN(amount) AS smallest_payment
                FROM payment;
            -> Example 2: Find the earliest payment date
                SELECT MIN(payment_date) AS earliest_payment
                FROM payment;
            -> Example 3: Using MIN with a WHERE condition
                SELECT MIN(amount) AS min_payment_2005
                FROM payment
                WHERE payment_date >= '2005-01-01'
                  AND payment_date < '2006-01-01';
        -> notes & best practices
            -> MIN() ignores NULL values in the column
            -> Useful with GROUP BY to find minimum per category
                Example:
                SELECT customer_id, MIN(amount) AS min_payment
                FROM payment
                GROUP BY customer_id;
            -> Can be combined with ORDER BY to highlight lowest results
    -> summary
        -> MAX(): returns the maximum value of a column
        -> MIN(): returns the minimum value of a column
        -> Both work on numeric and date/time columns
        -> Aggregate functions: summarize multiple rows into a single result
        -> Can be used with WHERE to filter data, GROUP BY to analyze per category, ORDER BY to sort results
        -> Syntax overview
            -- MIN function
            SELECT MIN(<YOUR_COLUMN>) AS <NEW_COLUMN_NAME>
            FROM <YOUR_TABLE>;

            -- MAX function
            SELECT MAX(<YOUR_COLUMN>) AS <NEW_COLUMN_NAME>
            FROM <YOUR_TABLE>;
"""