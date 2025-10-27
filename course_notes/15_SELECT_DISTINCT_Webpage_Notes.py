""" SELECT DISTINCT Webpage Notes 
    -> outline
        -> introduction
        -> how to use DISTINCT in SQL
        -> SQL SELECT DISTINCT real-world example
        -> summary: SQL SELECT DISTINCT statement
    -> SELECT DISTINCT <- to select rows that have unique data
        -> if we want to know information about unique data
        -> we can find out the number of distinct names in a table, if there are repeated first names in an actors table,
            for exmaple
        -> like Python sets, it removes the duplicates
    -> example
        -> SELECT DISTINCT birth_day, birth_month FROM employees; <- what HR can use to extract birthdays
            -> to select rows that have unique values in one or more columns
    -> general syntax:
        -> SELECT DISTINCT <YOUR_COLUMN_NAMES> FROM <YOUR_TABLE>;
"""