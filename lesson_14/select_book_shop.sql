-- Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.

SELECT p.user_id,date,first_name,last_name
FROM users INNER JOIN purchases p on users.id = p.user_id;

-- Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували, відсортувати дані за user_id.

SELECT users.id,users.first_name, users.last_name, title
FROM books,users INNER JOIN purchases on purchases.book_id = books.id AND
                                         purchases.user_id = users.id
ORDER BY users.id;

-- Написати запит, який виведе кількість покупок книжок для кожного user.

SELECT users.id, COUNT(user_id) as purchases_count
FROM users INNER JOIN purchases on purchases.user_id = users.id
GROUP BY users.id;

-- Написати запит, який виведе кількість покупок книжок для автора Rowling.

SELECT COUNT(book_id) as amount
FROM purchases INNER JOIN books b on b.id = purchases.book_id
WHERE author == 'Rowling';

-- Написати запит, який для кожного user порахує суму всіх покупок.

SELECT  users.id, users.first_name, users.last_name, SUM(price) as total_purchases
FROM users,books INNER JOIN purchases p on users.id = p.user_id AND
                                           books.id = p.book_id
GROUP BY user_id;

-- Написати запит, який виведе загальні суми продажів для кожного автора та кількість покупок.

SELECT  author, SUM(price) as total_purchases
FROM users,books INNER JOIN purchases p on users.id = p.user_id AND
                                           books.id = p.book_id
GROUP BY author;

-- Написати запит, який виведе всі назви книжок із кількістью їх продажів в порядку спадання кількості продажів

SELECT  title, COUNT(p.book_id) as total
FROM users u INNER JOIN books b INNER JOIN purchases p on u.id = p.user_id AND
                                           b.id = p.book_id
GROUP BY b.id;