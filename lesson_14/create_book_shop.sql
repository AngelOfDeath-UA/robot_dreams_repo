-- Create table users

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    age INTEGER
                                );

-- Create table publishing_house
CREATE TABLE IF NOT EXISTS publishing_house(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    rating INTEGER NOT NULL DEFAULT(5)
                                           );

-- Create table books
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER,
    price INTEGER NOT NULL,
    publishing_house_id INTEGER NOT NULL,
    FOREIGN KEY (publishing_house_id) references publishing_house(id)
                                );

-- Create table purchases
CREATE TABLE IF NOT EXISTS purchases(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    date TEXT,
    FOREIGN KEY (user_id) references users(id),
    FOREIGN KEY (book_id) references books(id)
                                    );
