--  Написати sql запит, який вибере усі записи із таблиці users старше 30 років.

SELECT *
FROM users
WHERE age > 30;

-- Написати sql запит, який виведе кількість записів в табліці users, що старше 30 років.

SELECT COUNT(id)
FROM users
WHERE age > 30;

-- Написати sql запит, який виведе інформацію про вік (кількість років) та кількість користувачів, які відповідають цьому віку.

SELECT age, COUNT(id) as users
FROM users
GROUP BY age;

-- Написати sql запит, який буде робити те саме, що і в завданні 3, але виводити дані відсортовані по кількості користувачів у спадаючому порядку та по віку у зростаючому порядку.

SELECT age, COUNT(id) as users
FROM users
GROUP BY age
ORDER BY users desc;

-- Модифікувати попередній запит таким чином, щоб з отриманого результату вибрати тільки ті записи, де значення users більше 1.

SELECT age, COUNT(id) as users
FROM users as users1
GROUP BY age
HAVING COUNT(id) > 1
ORDER BY users desc;

