SELECT DISTINCT
	f1.veznev,
    f2.utonev
FROM
	felhasznalo as f1
    JOIN felhasznalo as f2
		on f1.veznev = f2.veznev
    	and f1.utonev = f2.utonev 
    	and f1.id != f2.id
ORDER BY
	1,
    2;