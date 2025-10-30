""" Working with SQL Stored Procedures Webpage Notes
    -> outline
        -> introduction
        -> What is a SQL Stored Procedure?
        -> Why Use Stored Procedures?
        -> How Stored Procedures Work
        -> Components of a Stored Procedure
            -> Procedure Name
            -> Parameters (IN, OUT, INOUT)
            -> SQL Statements Block (BEGIN…END)
            -> Delimiters
        -> Creating a SQL Stored Procedure Step-by-Step
            -> Step 1: Define Procedure Parameters
            -> Step 2: Write and Execute Procedure Body
            -> Step 3: Refresh Schema to Register Procedure
        -> Key SQL Keywords in Stored Procedures
            -> CREATE PROCEDURE
            -> BEGIN
            -> END
            -> DELIMITER
            -> IN / OUT / INOUT
            -> RETURN
            -> CALL
        -> Calling Stored Procedures
            -> Basic Procedure Call
            -> Procedure Call with Parameters
            -> Capturing Output from OUT Parameters
        -> Advanced Features
            -> Using Variables Inside Procedures
            -> Conditional Logic (IF…ELSE)
            -> Loops (WHILE, REPEAT, LOOP)
            -> Error Handling (DECLARE…HANDLER)
            -> Transactions in Procedures (START TRANSACTION, COMMIT, ROLLBACK)
        -> Examples
            -> Simple Procedure (Top 10 Customers)
            -> Procedure with Input Parameter
            -> Procedure with Output Parameter
            -> Procedure with Conditional Logic
            -> Procedure with Loop
        -> Best Practices
            -> Keep Procedures Modular and Reusable
            -> Use Parameters for Flexibility
            -> Comment All Queries Inside Procedure
            -> Manage Transactions Carefully
            -> Optimize Queries for Performance
        -> Common Pitfalls and Notes
            -> Misuse of Delimiter
            -> Improper BEGIN…END Block Closure
            -> Forgotten Permissions (EXECUTE)
            -> NULL Values in Parameters
            -> Nested Procedures Complexity
        -> Summary: SQL Stored Procedures

    -> SQL Stored Procedures
        -> definition
            -> A SQL Stored Procedure is a **named collection of SQL statements** stored inside the database engine
            -> Acts like a **function** or **procedure** inside the database
            -> Can include **parameters**, **loops**, **conditional logic**, **transactions**, and multiple queries
            -> Stored procedures can be executed repeatedly without rewriting queries
        -> why use stored procedures?
            -> **Code Reusability:** Avoid duplicating complex queries
            -> **Simplified Access:** Non-technical users can call procedures without understanding SQL
            -> **Security:** Users can execute procedures without direct table access
            -> **Maintainability:** Centralized logic makes updating queries easier
            -> **Performance:** Precompiled execution plans in some DB engines
        -> how stored procedures work
            -> Step 1: Define a unique **procedure name**
            -> Step 2: Define **parameters** (optional)
            -> Step 3: Write the SQL statements inside **BEGIN…END**
            -> Step 4: Execute procedure using **CALL**
            -> Step 5: Optionally return values using **OUT parameters** or **SELECT statements**
        -> Components of a Stored Procedure
            -> **Procedure Name:** Identifier used to call the procedure
            -> **Parameters:**
                -> IN: Input value
                -> OUT: Output value
                -> INOUT: Input and Output
            -> **SQL Statements Block:** Enclosed in BEGIN…END; contains the executable logic
            -> **Delimiters:** Change default semicolon to avoid conflict with statements inside procedure
        -> Creating a SQL Stored Procedure Step-by-Step
            -> Step 1: Define Parameters
                -> Example: none
                    CREATE PROCEDURE GetTop10Customers()
            -> Step 2: Write and Execute Procedure Body
                DELIMITER //
                CREATE PROCEDURE GetTop10Customers()
                BEGIN
                    SELECT c.first_name, c.last_name, SUM(p.amount) AS total_payments
                    FROM customer c
                    JOIN payment p
                    ON c.customer_id = p.customer_id
                    GROUP BY c.customer_id
                    ORDER BY total_payments DESC
                    LIMIT 10;
                END //
                DELIMITER ;
            -> Step 3: Refresh Schema
                -> Refresh database schema to see procedure listed under **Stored Procedures**
        -> Key SQL Keywords
            -> **CREATE PROCEDURE:** Defines a new procedure
            -> **BEGIN / END:** Marks start and end of executable SQL block
            -> **DELIMITER:** Temporarily changes statement terminator
            -> **IN / OUT / INOUT:** Define parameter type
            -> **RETURN:** For functions (optional)
            -> **CALL:** Executes the stored procedure
        -> Calling Stored Procedures
            -> **Basic Call:** CALL sakila.GetTop10Customers();
            -> **With Input Parameters:**
                CALL GetCustomerPayments(15);
            -> **With OUT Parameters:**
                DECLARE total_amount DECIMAL(10,2);
                CALL GetCustomerTotal(15, @total_amount);
                SELECT @total_amount;
        -> Advanced Features
            -> **Variables Inside Procedures:**
                DECLARE variable_name datatype [DEFAULT value];
            -> **Conditional Logic:**
                IF condition THEN
                    -- statements
                ELSE
                    -- statements
                END IF;
            -> **Loops:**
                WHILE condition DO
                    -- statements
                END WHILE;
                REPEAT
                    -- statements
                UNTIL condition END REPEAT;
                LOOP
                    -- statements
                END LOOP;
            -> **Error Handling:**
                DECLARE handler_name CONDITION FOR SQLEXCEPTION
                    -- statements
            -> **Transactions:**
                START TRANSACTION;
                -- SQL statements
                COMMIT;
                ROLLBACK; -- on error
        -> Examples
            -> **Simple Procedure (Top 10 Customers)**
                See above in CREATE PROCEDURE example
            -> **Procedure with Input Parameter:**
                CREATE PROCEDURE GetCustomerPayments(IN cust_id INT)
                BEGIN
                    SELECT SUM(amount) AS total_payments
                    FROM payment
                    WHERE customer_id = cust_id;
                END;
            -> **Procedure with Output Parameter:**
                CREATE PROCEDURE GetCustomerTotal(IN cust_id INT, OUT total_amount DECIMAL(10,2))
                BEGIN
                    SELECT SUM(amount) INTO total_amount
                    FROM payment
                    WHERE customer_id = cust_id;
                END;
            -> **Procedure with Conditional Logic:**
                CREATE PROCEDURE CheckPaymentStatus(IN cust_id INT)
                BEGIN
                    IF (SELECT COUNT(*) FROM payment WHERE customer_id = cust_id) > 0 THEN
                        SELECT 'Customer has payments';
                    ELSE
                        SELECT 'Customer has no payments';
                    END IF;
                END;
            -> **Procedure with Loop:**
                CREATE PROCEDURE PrintNumbers()
                BEGIN
                    DECLARE i INT DEFAULT 1;
                    WHILE i <= 10 DO
                        SELECT i;
                        SET i = i + 1;
                    END WHILE;
                END;
        -> Best Practices
            -> Keep procedures **modular** and focused on a single task
            -> Use **parameters** for dynamic behavior
            -> Comment all queries inside procedures
            -> Use **transactions** when performing multiple DML statements
            -> Optimize queries for performance, especially with joins and aggregates
            -> Avoid overly complex nested procedures for readability
        -> Common Pitfalls
            -> Forgetting to reset **DELIMITER** back to semicolon
            -> Improper **BEGIN…END** closure
            -> Permissions: Users must have **EXECUTE** privilege
            -> Subquery errors inside procedures can propagate
            -> Misuse of NULL values in parameters
            -> Overuse can reduce portability between DB systems
        -> Summary
            -> SQL Stored Procedure = **saved, callable SQL query or set of queries**
            -> Simplifies repetitive tasks, enhances security, maintainability, and performance
            -> Key Keywords: CREATE PROCEDURE, BEGIN, END, DELIMITER, IN/OUT/INOUT, CALL
            -> Can include: variables, loops, conditional logic, error handling, transactions
            -> Procedures can be simple or highly complex depending on requirements
            -> Call with: CALL <DATABASE>.<PROCEDURE_NAME>(parameters)
            -> Ideal for: reporting, analytics, automation, encapsulating business logic
"""

