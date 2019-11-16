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
SELECT *, COUNT(*) AS 'TITLE_COUNT'
FROM authorpublishers
GROUP BY AUTHOR_ID
ORDER BY AUTHOR_ID DESC; 
--SUUUUUUUUUUUUUUUUUUUUUUUUUUM
-- CHALLENGE 3




-- CHALLENGE 4

