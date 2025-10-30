""" LIKE + Wildcards Webpage Notes
    -> outline
        -> introduction
        -> SQL LIKE Statement
        -> SQL Wildcard Characters
            -> % SQL Wildcard
            -> _ SQL Wildcard
        -> Advanced LIKE Usage
            -> Combining Multiple Wildcards
            -> Using NOT LIKE
            -> Case Sensitivity Considerations
        -> Summary: SQL LIKE Statement + SQL Wildcards
    -> SQL LIKE + Wildcards
        -> definition
            -> LIKE is an SQL operator used in the WHERE clause to perform pattern-based matching of string data
            -> Enables searching for data that meets partial patterns, rather than exact values
            -> Works with text/string columns and can be combined with wildcards for flexible queries
        -> usage context
            -> Searching for data with unknown characters or patterns
            -> Filtering results in reporting and analytics queries
            -> Can be used with aggregate functions (COUNT, SUM) to summarize filtered results
            -> Often combined with AND, OR, and NOT operators for advanced filtering
    -> SQL LIKE Statement
        -> purpose
            -> Filter data based on patterns in string/text columns
            -> Useful when the exact value is unknown or you want to match multiple similar values
        -> syntax
            -> SELECT <YOUR_COLUMNS>
               FROM <YOUR_TABLE>
               WHERE <YOUR_COLUMN> LIKE "<PATTERN>";
            -> <YOUR_COLUMNS>: Columns you want to retrieve
            -> <YOUR_TABLE>: Table to query
            -> <YOUR_COLUMN>: Column to perform pattern match on
            -> <PATTERN>: String pattern that may include wildcards (%) or (_)
        -> examples
            -> Example 1: Find all films starting with "P"
                SELECT title
                FROM film
                WHERE title LIKE "P%";
            -> Example 2: Find all films containing "cit" anywhere
                SELECT title
                FROM film
                WHERE title LIKE "%cit%";
            -> Example 3: Find all titles starting with "e" with "e" appearing at least three times
                SELECT title
                FROM film
                WHERE title LIKE "e%e%e";
    -> SQL Wildcard Characters
        -> % SQL Wildcard
            -> Represents zero or more characters of any type
            -> Can appear at the start, middle, or end of a string pattern
            -> Examples:
                -> "P%" → matches "Piano", "Planet", "Python"
                -> "%cit%" → matches "Citizen", "Critical", "Fiction"
            -> Useful for partial matching, finding substrings anywhere in a column
        -> _ SQL Wildcard
            -> Represents exactly one character
            -> Can be used for fixed-length pattern matching
            -> Examples:
                -> "e%e_e" → matches strings like "eve", "epeze", where one character exists between the last two "e"s
            -> Useful for strict pattern matching when the number of characters is known
        -> notes
            -> Multiple % and _ wildcards can be combined in a single pattern
            -> Patterns are matched from left to right
            -> Some databases (e.g., MySQL) treat LIKE as case-insensitive by default, but others (e.g., PostgreSQL) may be case-sensitive
    -> Advanced LIKE Usage
        -> Combining Multiple Wildcards
            -> Complex patterns can include multiple % and _ characters
            -> Example: "%a%e_" matches any string containing "a", then "e", followed by exactly one character
        -> Using NOT LIKE
            -> Excludes rows that match the given pattern
            -> Example: SELECT title FROM film WHERE title NOT LIKE "P%";
        -> Case Sensitivity Considerations
            -> In MySQL, LIKE is usually case-insensitive
            -> Use BINARY keyword in MySQL for case-sensitive matching: WHERE BINARY title LIKE "P%"
            -> In PostgreSQL, ILIKE can be used for case-insensitive matching
    -> summary
        -> LIKE is used inside WHERE clauses to filter text based on patterns
        -> % wildcard matches zero or more characters
        -> _ wildcard matches exactly one character
        -> Can combine multiple wildcards to create complex patterns
        -> NOT LIKE excludes patterns
        -> Be aware of case sensitivity depending on the database
        -> Syntax order: SELECT → FROM → WHERE <COLUMN> LIKE <PATTERN>
        -> Essential for flexible searches, partial matches, and string-based filtering
"""