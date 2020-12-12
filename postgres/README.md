This README will be used to document all things psotgres.

# Essential commands

List databases:
```sql
$ \l;
```

Create a database:
```sql
$ CREATE DATABASE [database name]
```

Use a database:
```sql
$ \c [database name]:
```

Show tables:
```sql
$ \dt
```

Show tables(verbose):
```sql
$ \dt+;
```

Delete a table:
```sql
$ DROP TABLE [table name];
```

Running sql from a dump file:
```sql
$ psql < schema.sql
```

# Create a table
General structure:
```sql
CREATE TABLE [table name] (
	[column name] [column setting] [column setting]...[column setting],
	[column name] [column setting]
);
```

Some example:
```sql
CREATE TABLE users (
	user_id INTEGER,
	password VARCHAR ( 50 )
);

INSERT INTO users VALUES
(0, 'password');
```



Some other example:
```sql
CREATE TABLE users (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);
```