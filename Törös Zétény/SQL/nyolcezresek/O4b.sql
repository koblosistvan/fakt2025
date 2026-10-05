SELECT
	nev, month(edatum) as hónap, COUNT(*)
FROM
	csucs
GROUP BY
	month(edatum);