/* Challenge 1 - Most Profiting Authors
Step 1: Calculate the royalties of each sales for each author */
SELECT
	titles.title_id,
	authors.au_id,
	titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 AS sales_royalty
FROM
	authors
JOIN titleauthor ON
	titleauthor.au_id = authors.au_id
JOIN titles ON
	titles.title_id = titleauthor.title_id
JOIN sales ON
	sales.title_id = titles.title_id;

/* Step 2: Aggregate the total royalties for each title for each author */
WITH royalties_per_sales_per_author AS (
SELECT
	titles.title_id,
	authors.au_id,
	titles.price*sales.qty*titles.royalty / 100 * titleauthor.royaltyper / 100 AS sales_royalty
FROM
	authors
JOIN titleauthor ON
	titleauthor.au_id = authors.au_id
JOIN titles ON
	titles.title_id = titleauthor.title_id
JOIN sales ON
	sales.title_id = titles.title_id)
SELECT
	royalties_per_sales_per_author.title_id,
	royalties_per_sales_per_author.au_id,
	SUM(sales_royalty) AS titles_royalty
FROM
	royalties_per_sales_per_author
JOIN titles ON
	royalties_per_sales_per_author.title_id = titles.title_id
JOIN titleauthor ON
	royalties_per_sales_per_author.au_id = titleauthor.au_id
GROUP BY
	titleauthor.au_id,
	titles.title_id;

/* Step 3: Calculate the total profits of each author */
WITH royalties_per_sales_per_author AS (
SELECT
	titles.title_id,
	authors.au_id,
	titles.price*sales.qty*titles.royalty / 100 * titleauthor.royaltyper / 100 AS sales_royalty
FROM
	authors
JOIN titleauthor ON
	titleauthor.au_id = authors.au_id
JOIN titles ON
	titles.title_id = titleauthor.title_id
JOIN sales ON
	sales.title_id = titles.title_id),
tot_royalties_tit_author AS (
SELECT
	royalties_per_sales_per_author.title_id,
	royalties_per_sales_per_author.au_id,
	SUM(sales_royalty) AS titles_royalty
FROM
	royalties_per_sales_per_author
JOIN titles ON
	royalties_per_sales_per_author.title_id = titles.title_id
JOIN titleauthor ON
	royalties_per_sales_per_author.au_id = titleauthor.au_id
GROUP BY
	titleauthor.au_id,
	titles.title_id)
SELECT
	tot_royalties_tit_author.au_id,
	tot_royalties_tit_author.titles_royalty + titles.advance*titleauthor.royaltyper / 100 AS total_profit
FROM
	tot_royalties_tit_author
JOIN titles ON
	tot_royalties_tit_author.title_id = titles.title_id
JOIN titleauthor ON
	tot_royalties_tit_author.au_id = titleauthor.au_id
ORDER BY
	total_profit DESC
LIMIT 3


/* Challenge 2 - Alternative Solution */
SELECT tot_royalties_tit_author.au_id,
tot_royalties_tit_author.titles_royalty + titles.advance*titleauthor.royaltyper / 100 AS total_profit
FROM
(
SELECT
	roy_sales_author.title_id,
	roy_sales_author.au_id,
	SUM(sales_royalty) AS titles_royalty
FROM
	(
	SELECT
		titles.title_id,
		authors.au_id,
		titles.price*sales.qty*titles.royalty / 100 * titleauthor.royaltyper / 100 AS sales_royalty
	FROM
		authors
	JOIN titleauthor ON
		titleauthor.au_id = authors.au_id
	JOIN titles ON
		titles.title_id = titleauthor.title_id
	JOIN sales ON
		sales.title_id = titles.title_id) AS roy_sales_author
JOIN titles ON
	roy_sales_author.title_id = titles.title_id
JOIN titleauthor ON
	roy_sales_author.au_id = titleauthor.au_id
GROUP BY
	titleauthor.au_id,
	titles.title_id) AS tot_royalties_tit_author
JOIN titles ON
tot_royalties_tit_author.title_id = titles.title_id
JOIN titleauthor ON
tot_royalties_tit_author.au_id = titleauthor.au_id
ORDER BY
total_profit DESC LIMIT 3;


/* Challenge 3 */
CREATE TABLE most_profiting_authors AS WITH royalties_per_sales_per_author AS (
SELECT
	titles.title_id,
	authors.au_id,
	titles.price*sales.qty*titles.royalty / 100 * titleauthor.royaltyper / 100 AS sales_royalty
FROM
	authors
JOIN titleauthor ON
	titleauthor.au_id = authors.au_id
JOIN titles ON
	titles.title_id = titleauthor.title_id
JOIN sales ON
	sales.title_id = titles.title_id),
tot_royalties_tit_author AS (
SELECT
	royalties_per_sales_per_author.title_id,
	royalties_per_sales_per_author.au_id,
	SUM(sales_royalty) AS titles_royalty
FROM
	royalties_per_sales_per_author
JOIN titles ON
	royalties_per_sales_per_author.title_id = titles.title_id
JOIN titleauthor ON
	royalties_per_sales_per_author.au_id = titleauthor.au_id
GROUP BY
	titleauthor.au_id,
	titles.title_id)
SELECT
	tot_royalties_tit_author.au_id,
	tot_royalties_tit_author.titles_royalty + titles.advance*titleauthor.royaltyper / 100 AS total_profit
FROM
	tot_royalties_tit_author
JOIN titles ON
	tot_royalties_tit_author.title_id = titles.title_id
JOIN titleauthor ON
	tot_royalties_tit_author.au_id = titleauthor.au_id
ORDER BY
	total_profit DESC
LIMIT 3;


