SELECT
	nev, month(edatum),
    COUNT(*)
FROM 
	csucs
GROUP BY
	month(edatum);