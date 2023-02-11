CREATE TABLE
    users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      UNIQUE (first_name, last_name)
    )
;

INSERT INTO
    users (first_name, last_name)
        VALUES
          ('John', 'Doe'),
          ('Jane', 'Doe'),
          ('Jim', 'Smith'),
          ('Emily', 'Johnson'),
          ('Michael', 'Brown')
    ;

