-- Insert into the users table
INSERT INTO users (first_name, last_name, age) VALUES
    ('John', 'Doe', 25),
    ('Jane', 'Doe', 30),
    ('Bob', 'Smith', 45),
    ('Samantha', 'Jones', 28),
    ('Tom', 'Brown', 33),
    ('Emily', 'Davis', 22),
    ('David', 'Lee', 50),
    ('Sarah', 'Kim', 29),
    ('Chris', 'Nguyen', 27),
    ('Avery', 'Wilson', 36);

-- Insert into the publishing_house table
INSERT INTO publishing_house (name, rating) VALUES
    ('Penguin Random House', 4),
    ('HarperCollins', 5),
    ('Simon & Schuster', 4),
    ('Macmillan Publishers', 3),
    ('Hachette Livre', 5),
    ('Wiley', 4),
    ('Pearson Education', 3),
    ('Scholastic', 5),
    ('Springer Nature', 4),
    ('Oxford University Press', 5);

-- Insert into the books table
INSERT INTO books (author, year, price, publishing_house_id) VALUES
    ('Jane Austen', 1813, 12, 2),
    ('Mark Twain', 1885, 10, 1),
    ('F. Scott Fitzgerald', 1925, 8, 2),
    ('George Orwell', 1949, 9, 3),
    ('J.D. Salinger', 1951, 10, 2),
    ('Harper Lee', 1960, 15, 1),
    ('Gabriel Garcia Marquez', 1967, 11, 4),
    ('Toni Morrison', 1987, 14, 2),
    ('J.K. Rowling', 1997, 20, 7),
    ('Suzanne Collins', 2008, 18, 8);

-- Insert into the purchases table
INSERT INTO purchases (user_id, book_id, date) VALUES
    (1, 4, '2023-02-14'),
    (2, 6, '2023-02-14'),
    (3, 2, '2023-02-13'),
    (4, 7, '2023-02-12'),
    (5, 5, '2023-02-11'),
    (6, 1, '2023-02-11'),
    (7, 10, '2023-02-10'),
    (8, 3, '2023-02-09'),
    (9, 8, '2023-02-08'),
    (10, 9, '2023-02-07');