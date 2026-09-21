SELECT 
	month(edatum) as honap, count(*) as elso_hoditas
FROM
	csucs
GROUP BY
	honap;