SELECT
	nev, magassag, orszag
FROM
	csucs
WHERE
	orszag LIKE '%Kína%'
ORDER BY
	nev;