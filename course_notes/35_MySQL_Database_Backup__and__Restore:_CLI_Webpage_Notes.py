""" MySQL Database Backup & Restore: CLI Webpage Notes
    -> outline
        -> Introduction
        -> What is a MySQL Database Backup and Restore?
        -> Why Backup & Restore is Critical
        -> Backup Concepts in MySQL
        -> Restore Concepts in MySQL
        -> Prerequisites for CLI Backup and Restore
        -> Step-by-Step MySQL Database Backup via CLI
            -> Login and Preparation
            -> Using mysqldump
            -> File Location, Permissions, and Verification
        -> Step-by-Step MySQL Database Deletion via CLI
            -> Drop vs Drop Schema
            -> Safety Considerations
        -> Step-by-Step MySQL Database Restore via CLI
            -> Creating the Target Schema
            -> Importing SQL Dump
            -> Monitoring Progress and Handling Large Databases
        -> Verifying the Restore
            -> Checking Databases and Tables
            -> Spot-checking Data Integrity
        -> Advanced Considerations
            -> Automating Backups with Scripts and Cron
            -> Incremental vs Full Backups
            -> Handling Large Databases and Binary Data
            -> Handling Users, Privileges, and Security
        -> Common Pitfalls and How to Avoid Them
        -> Best Practices
        -> MySQL CLI Commands Reference
        -> Summary

    -> MySQL Database Backup & Restore via CLI
        -> Introduction
            -> Backing up a database = exporting all its schema and data into a separate file (typically .sql)
            -> Restoring a database = importing a previously exported dump file back into MySQL
            -> CLI (Command Line Interface) is preferred for efficiency, scripting, automation, and large datasets
            -> Backup and Restore operations are critical for disaster recovery, migrations, and data sharing

        -> What is a MySQL Database Backup and Restore?
            -> Backup = mysqldump creates a text file containing all SQL commands necessary to recreate the database tables, constraints, indexes, triggers, and data
            -> Restore = executing the SQL commands from the dump file to rebuild the database in MySQL
            -> Backup can be:
                -> Logical: SQL dump of schema + data
                -> Physical: Copying actual data files (requires server downtime)
            -> Restore can be:
                -> Full restore from dump
                -> Partial restore (subset of tables or data)

        -> Why Backup & Restore is Critical
            -> Prevent data loss from:
                -> Human error (accidental deletes)
                -> Hardware failure or corruption
                -> Software errors or bugs
                -> Security incidents
            -> Facilitate migrations between servers or MySQL versions
            -> Enable testing on development or staging environments
            -> Provide point-in-time recovery (with regular backups)

        -> Backup Concepts in MySQL
            -> mysqldump syntax: exports SQL commands to recreate the database
            -> Can include:
                -> Schema only (`--no-data`)
                -> Data only (`--no-create-info`)
                -> Both schema + data (default)
            -> Options:
                -> `--routines` for stored procedures/functions
                -> `--triggers` to include triggers
                -> `--events` to include scheduled events
                -> `--single-transaction` to avoid locking large tables during backup
            -> Output file should be securely stored, optionally compressed:
                -> `gzip ~/Desktop/sakila_backup.sql` → `sakila_backup.sql.gz`

        -> Restore Concepts in MySQL
            -> Restore involves executing SQL commands from the backup file into a target schema
            -> Target schema must exist or be created prior to import
            -> Restoration is transactional if using InnoDB (atomic updates)
            -> For very large databases, consider splitting dump or using `mysqlpump` for parallel import

        -> Prerequisites for CLI Backup and Restore
            -> MySQL server installed and running
            -> Root or privileged user access
            -> Access to CLI / Terminal
            -> Sufficient disk space for backups
            -> Knowledge of database names and tables
            -> Optional: understanding of Linux/Mac shell for file operations

        -> Step-by-Step MySQL Database Backup via CLI
            -> Login and Preparation
                1. Open terminal / CLI
                2. Login to MySQL shell:
                    mysql -u root -p
                3. Enter root password
                4. Check databases:
                    SHOW DATABASES;
                5. Exit shell:
                    EXIT;
            -> Using mysqldump
                1. Run the mysqldump command:
                    mysqldump -u root -p sakila > ~/Desktop/sakila_backup.sql
                    -> `-u root` = username
                    -> `-p` prompts for password
                    -> `sakila` = database name
                    -> `>` redirects output to file
                2. Optional flags:
                    --routines → include stored procedures
                    --triggers → include triggers
                    --events → include scheduled events
                    --single-transaction → avoid locking tables during dump
                3. Verify file creation:
                    ls -al ~/Desktop
                4. Optional: view contents:
                    cat ~/Desktop/sakila_backup.sql

            -> File Location, Permissions, and Verification
                -> Backup file should be stored securely
                -> Set proper permissions to prevent unauthorized access:
                    chmod 600 ~/Desktop/sakila_backup.sql
                -> Backup file can be compressed for storage efficiency:
                    gzip ~/Desktop/sakila_backup.sql

        -> Step-by-Step MySQL Database Deletion via CLI
            -> Drop vs Drop Schema
                -> DROP DATABASE sakila;
                -> DROP SCHEMA sakila;
                -> Both permanently remove all tables, data, triggers, routines in the schema
            -> Safety Considerations
                -> Only delete after verifying backup exists
                -> Cannot be undone without a backup
                -> Use `SHOW DATABASES;` to confirm deletion

        -> Step-by-Step MySQL Database Restore via CLI
            -> Creating the Target Schema
                -> Login to MySQL shell:
                    mysql -u root -p
                -> Create empty database:
                    CREATE SCHEMA sakila;
                -> Exit shell:
                    EXIT;
            -> Importing SQL Dump
                -> Restore using:
                    mysql -u root -p sakila < ~/Desktop/sakila_backup.sql
                -> Notes:
                    -> `<` operator reads the SQL file and executes commands
                    -> Large databases may take several minutes
                    -> Monitor errors during import for issues such as missing privileges
            -> Monitoring Progress and Handling Large Databases
                -> Consider splitting large dumps using `split` command
                -> Use `mysql --max_allowed_packet=512M -u root -p sakila < dump.sql` for large BLOBs
                -> Use `mysqlpump` for parallel restore if available

        -> Verifying the Restore
            -> Check databases:
                SHOW DATABASES;
            -> Use restored database:
                USE sakila;
            -> Verify table data:
                SELECT * FROM actor LIMIT 10;
            -> Spot-check totals and counts for correctness:
                SELECT COUNT(*) FROM customer;
                SELECT SUM(amount) FROM payment;
            -> Compare with backup file or previous export to confirm integrity

        -> Advanced Considerations
            -> Automating Backups
                -> Use cron jobs in Linux:
                    0 2 * * * mysqldump -u root -pPASSWORD sakila > /path/to/backup/sakila_$(date +\%F).sql
                -> Schedule daily or weekly backups
            -> Incremental vs Full Backups
                -> Full backup = complete schema + data
                -> Incremental backup = captures changes since last backup
                -> MySQL binary logs can be used for incremental backup
            -> Handling Large Databases
                -> Use compression: gzip or bzip2
                -> Increase `max_allowed_packet` if errors on large inserts
                -> Use `--single-transaction` with InnoDB tables to avoid table locks
            -> Handling Users, Privileges, Security
                -> Backup does not automatically backup users or privileges
                -> Use `mysql -u root -p -e "SELECT * FROM mysql.user;" > users_backup.sql` to backup users
                -> Secure backups to prevent unauthorized access to credentials and data

        -> Common Pitfalls
            -> Forgetting password or using wrong credentials
            -> Overwriting backup files unintentionally
            -> Importing backup into wrong database/schema
            -> Not including stored procedures or triggers in backup
            -> Large databases failing due to max_allowed_packet limits
            -> Mistaking DROP DATABASE as recoverable without a backup

        -> Best Practices
            -> Always verify backups and test restores
            -> Use versioned backup files with timestamps
            -> Store backups offsite or in cloud storage for disaster recovery
            -> Automate regular backups
            -> Include schema, data, triggers, routines, and events for complete recovery
            -> Document backup and restore procedures for team use

        -> MySQL CLI Commands Reference
            -> Backup / Export:
                mysqldump -u <USERNAME> -p <DATABASE_NAME> > <PATH_TO_FILE.sql>
                mysqldump --routines --triggers --events -u <USERNAME> -p <DATABASE_NAME> > <PATH_TO_FILE.sql>
            -> Delete Database:
                DROP DATABASE <DATABASE_NAME>;
                DROP SCHEMA <DATABASE_NAME>;
            -> Create Database:
                CREATE SCHEMA <DATABASE_NAME>;
            -> Restore / Import:
                mysql -u <USERNAME> -p <DATABASE_NAME> < <PATH_TO_FILE.sql>
            -> Verify Databases:
                SHOW DATABASES;
            -> Verify Table Contents:
                SELECT * FROM <TABLE_NAME> LIMIT 10;

        -> Summary
            -> Backup = export database schema + data using mysqldump
            -> Restore = import SQL dump file into MySQL schema
            -> CLI allows fast, scriptable, repeatable backups
            -> Always verify backups and restores
            -> Follow best practices for security, automation, and disaster recovery
"""