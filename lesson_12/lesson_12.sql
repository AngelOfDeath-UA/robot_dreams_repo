CREATE TABLE
    users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      age INTEGER,
      UNIQUE (first_name, last_name)
    )
;

INSERT INTO
    users (first_name, last_name, age)
        VALUES
          ('John', 'Doe', 23),
          ('Jane', 'Doe', 18),
          ('Jim', 'Smith', 27),
          ('Emily', 'Johnson', 19),
          ('Michael', 'Brown', 33)
    ;

