This README will be used to document all things psotgres.

# Essential commands

List databases:
```
$ \l;
```

Use a database:
```
$ \c [database name]:
```

Show tables:
```
$ \dt
```

Show tables(verbose):
```
$ \dt+;
```

# Create a table
Some example:
```
CREATE TABLE users (
	user_id INTEGER,
	password VARCHAR ( 50 )
);
```

Some other example:
```
CREATE TABLE users (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);
```