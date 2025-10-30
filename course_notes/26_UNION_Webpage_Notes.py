"""UNION Webpage Notes
    -> outline
        -> introduction
        -> SQL Union vs. Union All
        -> SQL Union vs Join
        -> SQL Union Example
        -> SQL Union All Example
        -> Summary: SQL Union
    -> UNION
        -> definition
            -> The SQL UNION statement combines the results between two or more SELECT statements
            -> Only returns distinct results by default
        -> UNION ALL
            -> A modification of UNION
            -> Returns all results, including duplicates
        -> usage context
            -> Useful for merging data from multiple tables vertically
    -> SQL Union vs. Union All
        -> difference
            -> UNION removes duplicates in the result set
            -> UNION ALL includes duplicates in the result set
    -> SQL Union vs Join
        -> difference
            -> UNION combines result sets vertically
            -> JOIN combines result sets horizontally
        -> example visualization
            -> UNION: stacking rows from different SELECTs
            -> JOIN: adding columns by matching keys
    -> SQL Union Example
        -> scenario
            -> Suppose you want a list of all first and last names from both actors and customers
        -> query
            -> SELECT first_name, last_name
                FROM actor
              UNION
                SELECT first_name, last_name
                FROM customer;
        -> notes
            -> Returns a single list of all actors and customers
            -> Duplicate names are removed
    -> SQL Union All Example
        -> scenario
            -> Similar to UNION example, but you want to include duplicates
        -> query
            -> SELECT first_name, last_name
                FROM actor
              UNION ALL
                SELECT first_name, last_name
                FROM customer;
        -> notes
            -> Returns all results, including duplicates
            -> Example result count: 799 vs 797 in UNION
    -> summary
        -> UNION
            -> Combines results of two or more SELECT statements
            -> Returns distinct results by default
        -> UNION ALL
            -> Returns all results, including duplicates
        -> Difference: inclusion/exclusion of duplicates
        -> UNION vs JOIN
            -> UNION: vertical combination of result sets
            -> JOIN: horizontal combination of result sets
        -> Requirement
            -> Columns chosen for UNION must have compatible data types
        -> SQL Union Syntax
            -> SELECT <YOUR_COLUMNS>
               FROM <YOUR_TABLE_1>
               UNION
               SELECT <YOUR_COLUMNS>
               FROM <YOUR_TABLE_2>
"""