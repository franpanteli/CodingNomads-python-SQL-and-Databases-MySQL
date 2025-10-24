""" Create a DB Schema + Tables Webpage Notes 
    -> outline
        -> introduction
        -> how to create a database schema in MySQL
            -> a database schema refers to how the tables in a relational database are connected
                -> e.g, by their columns
        -> how to add a table using MySQL: create table
            -> MySQL is an application for Relational Database Management (RDBMS)
            -> the language it uses to query the database is SQL (Structured Query Language)
            -> MySQL can be run in the CLI, or using an open-source application called MySQL Workbench
                -> this contains a GUI
        -> Summary: create a database schema and table in MySQL
    -> introduction
        -> to create a relational database schema with MySQL, we first need to connect to the RDBMS
            -> relational database management system
            -> we then need to create the tables and relationships between them that are required for the application
            -> IN THIS LESSON, WE ARE CREATING A MYSQL DATABASE AND TABLE
    -> how to create a database schema in MySQL
        -> steps for usingMySQL to create a database schema in Mac, Windows and Linux
        -> install MySQL on the machine
            -> this is checked, by running `mysql --version` from the CLI
            -> if this isn't installed, refer to their instructions on how to install MySQL
        -> run MySQL on the machine
            -> Mac
                -> sudo /usr/local/mysql/support-files/mysql.server start
                -> sudo launchctl load -F /Library/LaunchDaemons/com.oracle.oss.mysql.mysqld.plist
            -> Linux 
                -> /etc/init.d/mysqld start
                -> service mysqld start
                -> service mysql start
            -> Linux


"""