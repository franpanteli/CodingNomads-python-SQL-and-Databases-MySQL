""" SUM, COUNT and AVERAGE Webpage Notes 
    -> outline
        -> introduction
        -> SQL SUM
        -> SQL SUM Example with Conditions
        -> SQL COUNT
        -> SQL AVG
        -> Summary: SQL SUM, SQL COUNT, SQL AVG
    -> SQL SUM / COUNT / AVG
        -> definition
            -> SQL provides helper functions to perform calculations on numeric columns
            -> SUM(): calculates the total sum of a column
            -> COUNT(): counts the number of records in a column
            -> AVG(): calculates the average value of a column
        -> usage context
            -> Useful for reporting, analytics, and summarizing data
            -> Works in MySQL and all common relational databases
    -> SQL SUM
        -> purpose
            -> Adds up all the values of a given numeric column
        -> example query
            -> SELECT SUM(amount) FROM payment;
        -> notes
            -> Returns a column named SUM(amount) by default
            -> Column names can be renamed using AS
                -> Example: SELECT SUM(amount) AS total_revenue FROM payment;
    -> SQL SUM Example with Conditions
        -> purpose
            -> Calculate sum based on specific conditions or filters
        -> example query
            -> SELECT SUM(amount) AS total_revenue_2005
               FROM payment
               WHERE payment_date > "2005-01-01"
                 AND payment_date < "2006-01-01";
        -> notes
            -> Only sums payments within the year 2005
            -> AS keyword used to rename result column to total_revenue_2005
    -> SQL COUNT
        -> purpose
            -> Counts total number of records that match a query
        -> example queries
            -> Count payments in 2005:
                SELECT COUNT(amount) AS num_payment_2005
                FROM payment
                WHERE payment_date > "2005-01-01"
                  AND payment_date < "2006-01-01";
            -> Count total customers:
                SELECT COUNT(customer_id) AS customers
                FROM customer;
        -> notes
            -> Useful for totals, frequency counts, or record checks
    -> SQL AVG
        -> purpose
            -> Calculates the average of a numeric column
        -> example query
            -> SELECT AVG(amount) AS avg_payment
               FROM payment;
        -> notes
            -> AS keyword allows you to rename the result column to something meaningful
            -> Provides insight into typical values in a dataset
    -> summary
        -> SQL SUM(): sums numeric column values
        -> SQL COUNT(): counts number of records in a column
        -> SQL AVG(): computes average of a numeric column
        -> AS keyword
            -> Allows renaming of columns created by these functions
        -> syntax overview
            -- SUM function
            SELECT SUM(<YOUR_COLUMNS>)
            FROM <YOUR_TABLE>;

            -- COUNT function
            SELECT COUNT(<YOUR_COLUMNS>)
            FROM <YOUR_TABLE>;

            -- AVG function with optional AS
            SELECT AVG(<YOUR_COLUMNS>) AS <YOUR_NEW_COLUMN_NAME>
            FROM <YOUR_TABLE>;
"""











