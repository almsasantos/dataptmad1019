-- CHALLENGE 1
SELECT authors.au_id AS 'AUTHOR_ID',
authors.au_lname AS 'LAST_NAME',
authors.au_fname AS 'FIRST_NAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLISHER'
FROM titles
JOIN publishers ON publishers.pub_id = titles.pub_id
JOIN titleauthor ON titleauthor.title_id = titles.title_id
JOIN authors ON authors.au_id = titleauthor.au_id;


-- CHALLENGE 2
WITH
authorpublishers AS
(
SELECT authors.au_id AS 'AUTHOR_ID',
authors.au_lname AS 'LAST_NAME',
authors.au_fname AS 'FIRST_NAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLISHER'
FROM titles
JOIN publishers ON publishers.pub_id = titles.pub_id
JOIN titleauthor ON titleauthor.title_id = titles.title_id
JOIN authors ON authors.au_id = titleauthor.au_id
)
SELECT *, 
COUNT(*) AS 'TITLE_COUNT'
FROM authorpublishers
GROUP BY AUTHOR_ID
ORDER BY AUTHOR_ID DESC;


-- CHALLENGE 3
SELECT authors.au_id AS 'AUTHOR_ID',
authors.au_lname AS 'LAST_NAME',
authors.au_fname AS 'FIRST_NAME',
SUM(titles.ytd_sales) AS 'TOTAL'
FROM titles
JOIN titleauthor ON titleauthor.title_id = titles.title_id
JOIN authors ON authors.au_id = titleauthor.au_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC LIMIT 3;


-- CHALLENGE 4
SELECT authors.au_id AS 'AUTHOR_ID',
authors.au_lname AS 'LAST_NAME',
authors.au_fname AS 'FIRST_NAME',
IFNULL(titles.ytd_sales, 0) AS 'TOTAL'
FROM authors
LEFT JOIN titleauthor ON titleauthor.au_id = authors.au_id
LEFT JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC;


-- BONUS CHALLENGE
SELECT authors.au_id AS 'AUTHOR_ID',
authors.au_lname AS 'LAST_NAME',
authors.au_fname AS 'FIRST_NAME',
(titles.advance + (titles.price * titles.ytd_sales *(titleauthor.royaltyper/100))) AS 'PROFIT'
FROM titles
JOIN titleauthor ON titles.title_id = titleauthor.title_id
JOIN authors ON authors.au_id = titleauthor.au_id
GROUP BY titleauthor.royaltyper
ORDER BY PROFIT DESC LIMIT 3;