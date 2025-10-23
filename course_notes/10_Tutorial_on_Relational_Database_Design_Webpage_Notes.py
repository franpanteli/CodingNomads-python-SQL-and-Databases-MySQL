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
                #2 MANY-TO-MANY
                #3 ONE-TO-ONE
        -> step 4: redefine and normalise the design
            ->
        -> resources and references
            1. "Database design basics (Microsoft Access 2007)", available at http://office.microsoft.com/en-us/access/HA012242471033.aspx.
            2. Paul Litwin, "Fundamentals of Relational Database Design", available at http://www.deeptraining.com/litwin/dbdesign/FundamentalsOfRelationalDatabaseDesign.aspx.
            3. Codd E. F., "A Relational Model of Data for Large Shared Data Banks", Communications of the ACM, vol. 13, issue 6, pp. 377–387, June 1970.

"""