SELECT
	nev,magassag/1000 as "Magasság km-ben", orszag
FROM
	csucs
ORDER BY magassag DESC;