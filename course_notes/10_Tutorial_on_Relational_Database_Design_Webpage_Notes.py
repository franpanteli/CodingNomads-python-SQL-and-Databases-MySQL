""" Tutorial on Relational Database Design Webpage Notes 
    -> outline
        -> introduction
        -> database design objective
        -> relational database design process
            -> step 1: define the purpose of the database
            -> step 2: gather data, organise in tables and specify the primary keys
            -> step 3: create relationships among tables
                -> one-to-many
                -> many-to-many
                -> one-to-one
            -> step 4: refine and normalise the design
                -> normalisation
                -> first normal form
                -> second normal form
                -> third normal form
                -> higher normal form
                -> integrity rules
                -> column indexing
            -> references and resources
    -> introduction
        -> this is an explanation of why relational databases are considered relational
        -> this is a quick-start tutorial
        -> relational databases were proposed by Edgar Codd
            -> IBM research
            -> 1916
        -> the dominant database model for commercial applications
            -> in comparison to other database models <- hierarchical, network and object models
        -> RDBMS <- Relational Database Management System
            -> Oracle, IBM DB2, Microsoft SQL Server
            -> there are free / open source ones <- MySQL, mSQL (mini SQL), embedded JavaDB (Apache Derby)
        -> RELATIONAL DATABASES ORGANISE DATA IN SPREADSHEETS
            -> TABLES ARE THE RELATIONS
            -> A COLUMN IS CALLED A FIELD, OR ATTRIBUTE
        -> relationships can be created among the tables
            -> this enables the database to store large amounts of data and retrieve selected data
            -> SQL <- STRUCTURED QUERY LANGUAGE
    -> database design objective
        -> we-designed databases will:
            -> eliminate data redundancy
                -> the same piece of data isn't stored in the same place
                -> duplicate data wastes storage space and leads to insecurities
            -> ensure data integrity
            -> ensure the accuracy of data
    -> relational database design process
        -> about
            -> DATABASE DESIGN requires many decisions
                -> IT IS CONTEXT DEPENDENT
                -> for a particular application
                    -> no two are the same
                    -> guidelines, in terms of what not to do, rather than what to do - are provided in making the design
                        decision, but the choices are individual
        -> step 1: define the purpose of the database (requirement analysis)
            -> gather the requirements
            -> define the database objective
            -> this can require drafting input forms / queries, etc
        -> step 2: gather data, organise tables and specify the primary keys
            -> we decide the purpose of the database
            -> then we the data it stores
                -> we want to divide this into tables
                -> WE CHOOSE ONE COLUMN, OR MULTIPLE, AS THE PRIMARY KEY
            -> primary key
                -> use and benefits
                    -> IN THE RELATIONAL MODEL, THE TABLE CAN'T CONTAIN DUPLICATE ROWS
                        -> this would create ambiguities
                        -> WE WANT DATA TO BE UNIQUE - THIS IS ONE OF THE REASONS WE USE A PRIMARY KEY
                    -> A PRIMARY KEY IS CALLED A SIMPLE KEY, IF IT'S A SINGLE COLUMN
                        -> IT IS CALLED A COMPOSITE KEY IF IT IS MADE UP OF SEVERAL COLUMNS
                    -> RDBMS'S build an index on the primary key
                        -> it is used to search for data
                        -> this is also used to reference other tables
                    -> WE HAVE TO DECIDE WHICH COLUMN IN THE DATABASE CONTAINS THIS
                    -> it is usually a single column
                        -> it can also be made up of several columns
                        -> it should be set with as little columns as possible
                -> properties
                    -> ITS VALUES HAVE TO BE UNIQUE
                        -> no duplicate values
                        -> there could be two customers with the same name, for example
                    -> the primary key will always have a value - it can't be NULL
                    -> it should be simple and familiar
                    -> IT'S VALUE SHOULDN'T BE CHANGED, BECAUSE IT IS REFERENCED IN THE TABLES
                        -> it is used to reference other tables
                        -> if you change it's value, you have to change all the references
                        -> the references will otherwise be lost
                    -> it uses an integer (number) type
                        -> it could be other types - e.g, text
                        -> IT IS BEST TO USE NUMBERS AS THE PRIMARY KEY, FOR EFFICIENCY
                    -> IT COULD TAKE AN ARBITRARY NUMBER - E.G, AN AUTO-INCREMENT
                        -> an integer for the primary key
                        -> IT IS FACT-LESS - IT CONTAINS NO FACTUAL INFORMATION
                -> example
                    -> a table called `customers`, that contains columns: lastName, firstName, phoneNumber, address,
                        city, state, zipCode
                    -> we can use most of the columns as the primary key
                    -> we don't use the columns with data that can change
                        -> personal information <- address / phone number
        -> step 3: create relationships among tables
            -> RELATIONAL DATABASE TABLES ARE CONNECTED
                -> we care about the relationship between tables
                -> we want to identify the relationship between tables
            -> TYPES OF RELATIONS BETWEEN TABLES
                #1 ONE-TO-MANY
                    -> examples
                        -> MANY STUDENTS TO ONE TEACHER - 'class roster'
                        -> many employees to one manager
                        -> many orders to one customer
                    -> about
                        -> THIS IS NOT REPRESENTED BY A SINGLE TABLE
                            -> THERE CAN BE A SINGLE TEACHERS TABLE, BUT WE ALSO NEED ANOTHER TABLE FOR ALL THE STUDENTS
                                FOR THAT ONE TEACHER
                            -> IF WE USED ONE TABLE FOR THIS EXAMPLE, THEN DATA WOULD BE REPLICATED - AND THIS ISN'T
                                ALLOWED
                        -> we need to define two tables
                            -> one for hte teachers and one for the classes
                            -> AND THEN A PRIMARY KEY, FOR EXAMPLE TEACHER ID, TO RELATE / LINK THE TABLES (RELATIONAL
                                DATABASE)
                            -> this is a one to many relationship
                            -> WE HAVE PRIMARY KEYS, TEACHERS, AND FOREIGN KEYS, THE CLASSES THAT THEY TEACH (ONE:MANY)
                #2 MANY-TO-MANY
                    -> examples
                        -> ordering things
                            -> a customer can contain one or many products
                            -> products can appear in many orders
                        -> bookstore databases
                            -> books written by one or more authors
                            -> an author can write zero - more books
                    -> ordering things (continued)
                        -> designing this database
                        -> Products and Orders tables
                            -> the first contains information about the products
                            -> the orders table contains information about the customer's orders
                            -> we don't know the amount of orders that will be made, or the amount of customers we will
                                have
                            -> WE CREATE A JUNCTION TABLE
                                -> EACH ROW REPRESENTS AN ITEM OF A PARTICULAR ORDER
                                    -> EACH ROW REPRESENTS AN ITEM OF A PARTICULAR ORDER
                                -> the primary key consists of two columns in this case
                                    -> orderID and productID <- THESE NUMBERS ARE LITERALLY USED IN THE DATABASE
                                    -> THEY ARE ALSO FOREIGN KEYS IN THE JUNCTION TABLE
                            -> THE MANY-TO-MANY RELATIONSHIP IS IMPLEMENTED AS TWO MANY-TO-ONE RELATIONSHIPS
                                -> THIS IS DONE BY IMPLEMENTING THE JUNCTION TABLE
                                    -> an order has many items in OrderDetails <- it is ordered many times
                                    -> an OrderDetails item belongs to one particular order
                                    -> a product appears in many OrderDetails
                                        -> each OrderDetails item specified one product
                #3 ONE-TO-ONE
                    -> in a product sales database
                        -> one product:information about it
                            -> images
                            -> descriptions
                            -> comments
                            -> this information is kept in the Products table
                            -> LARGE DATA CAN DEGRADE THE PERFORMANCE OF THE DATABASE
                    -> we create a table, to store the optional data
                        -> a record is only created for items with the optional data
                        -> THERE CAN BE GAPS IN THE DATABASE, JUST NO DUPLICATES
                        -> WE ALSO HAVE TO BE CAREFUL THAT THE DATA USED FOR THE PRIMARY KEY WON'T CHANGE, AND IS
                            PREFERABLY A NUMBER FOR EFFICIENCY
                        -> this is done with two extra tables, in a one-to-one relationship
                        -> for every tow in the PARENT TABLE, there is at most one row in the child table
                        -> SOME DATABASES LIMIT THE NUMBER OF COLUMNS THAT CAN BE CREATED INSIDE THE TABLE
                            -> A ONE-TO-ONE RELATIONSHIP SHOULD BE USED FOR THIS, TO SPLIT THE DATA INTO TWO TABLES
                    -> THESE RELATIONSHIPS ARE ALSO USEFUL FOR STORING SENSITIVE DATA IN A SECURE WAY
                        -> NON-SENSITIVE DATA IN THE MAIN TABLE
                    -> column data types
                        -> we need to choose appropriate data for each column
                            -> integers, floating-point numbers, string (or text), date/time, binary, collection (such
                                as enumeration and set)
        -> step 4: redefine and normalise the design
            -> editing the design of the database
                -> adding columns
                -> creating new tables for one-to-one relationships
                -> splitting large tables into smaller ones
            -> normalisation
                -> normalisation
                    -> NORMALISING THE DATA IN THE TABLE
                -> normal forms
                    -> FIRST NORMAL FORM
                        -> A TABLE IS 1NF IF EVERY CELL CONTAINS A SINGLE VALUE, NOT A LIST OF THEM
                        -> THIS IS ALSO CALLED ATOMIC
                        -> THIS PROHIBITS REPEATING GROUP OF COLUMNS
                        -> to maintain this, we want to create another table, using a one-to-many relationship
                    -> Second Normal Form (2NF)
                        -> a table is 2NF, if it is 1NF AND EVERY NON-KEY COLUMN IS FULLY DEPENDENT ON THE PRIMARY KEY
                        -> if the primary key is made up of several columns, every non-key column will depend on the
                            entire set and not part of it
                            -> e.g, ONE PRIMARY KEY CAN BE MADE UP OF TWO DIFFERENT TABLES
                                -> we are thinking about dependencies here
                    -> Third Normal Form (3NF)
                        -> A TABLE IS 3NF, IF IT IS 2NF AND THE NON-KEY COLUMNS ARE INDEPENDENT OF EACH OTHER
                            -> THE NON-KEY COLUMNS ARE DEPENDENT ONLY ON THE PRIMARY-KEY
                            -> e.g, a products table with a primary key and unit price column
                                -> ONE COLUMN (DISCOUNT RATE) DOES NOT BELONG TO THE UNIT PRICE TABLE, BECAUSE IT IS NOT
                                    A PART OF THE PRIMARY KEY
                    -> Higher Normal Form
                        -> where 3NF is inadequate
                        -> this leads to higher Normal form
                            -> BOYCE / CODD Normal form
                        -> fourth and fifth Normal forms also exist
                        -> WE CAN BREAK THE NORMALISATION RULES
                            -> NORMALISING A DATABASE IS NOT THE SAME AS IN STATISTICS, IT IS TO DO WITH DEPENDENCIES
                                OF THE DATA WE USE AS THE PRIMARY KEYS IN ITS TABLES
                            -> e.g, creating a column to do ith the price of orders that can be derived from the
                                orderDetails table
                                    -> WE CAN USE ONE PIECE OF INFORMATION TO BUILD UP A TABLE ON ANOTHER - IT HAS TO BE
                                        NON-DEPENDENT IN THIS FORM (THIS IS WHAT DEPENDENCY IN THE DATA REFERS TO)
                                -> this is to do with the decisions we are making
                                -> it is context-dependent, for example on the different ways that SQL will be leveraged
                                    on behalf of the user
            -> INTEGRITY RULES
                -> WE ALSO NEED TO CHECK THE INTEGRITY OF THE DESIGN
                -> ENTITY INTEGRITY RULE <- THE PRIMARY CANNOT CONTAIN NULL VALUES (OTHERWISE, THEY CAN BE REPEATED, AND
                    ARE NOT UNIQUE)
                -> WITH A COMPOSITE KEY MADE OF SEVERAL COLUMNS, NONE OF THE COLUMNS CAN CONTAIN NULL
                    -> MOST RDBMS'S ENFORCE THIS RULE
            -> REFERENTIAL INTEGRITY RULE
                -> EACH FOREIGN KEY MUST BE MATCHED TO A PRIMARY KEY VALUE, EITHER IN THE PARENT / REFERENCED TABLE
                    -> YOU CAN INSERT A ROW WITH A FOREIGN KEY IN THE CHILD TABLE, ONLY IF THE VALUE EXISTS IN THE
                        PARENT TABLE
                    ->     
        -> resources and references
            1. "Database design basics (Microsoft Access 2007)", available at http://office.microsoft.com/en-us/access/HA012242471033.aspx.
            2. Paul Litwin, "Fundamentals of Relational Database Design", available at http://www.deeptraining.com/litwin/dbdesign/FundamentalsOfRelationalDatabaseDesign.aspx.
            3. Codd E. F., "A Relational Model of Data for Large Shared Data Banks", Communications of the ACM, vol. 13, issue 6, pp. 377–387, June 1970.

"""