-- Удаление всех записей из таблиц User, Book и Purchase
DELETE FROM user;
DELETE FROM book;
DELETE FROM purchase;

-- Вставка 5 тестовых значений в таблицу User
INSERT INTO user (first_name, age, password)
VALUES ('John', 25, 'pass1'),
       ('Alice', 30, 'pass2'),
       ('Bob', 22, 'pass3'),
       ('Eve', 35, 'pass4'),
       ('Charlie', 28, 'pass5');

-- Вставка 5 тестовых значений в таблицу Book
INSERT INTO book (title, author, year, price)
VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960, 10),
       ('1984', 'George Orwell', 1949, 15),
       ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 20),
       ('Pride and Prejudice', 'Jane Austen', 1813, 12),
       ('The Catcher in the Rye', 'J.D. Salinger', 1951, 18);

-- Вставка 5 тестовых значений в таблицу Purchase
INSERT INTO purchase (user_id, book_id, date)
VALUES (1, 1, '2022-07-11'),
       (2, 3, '2022-07-28'),
       (3, 2, '2022-08-03'),
       (4, 4, '2023-01-22'),
       (5, 5, '2023-02-02');
