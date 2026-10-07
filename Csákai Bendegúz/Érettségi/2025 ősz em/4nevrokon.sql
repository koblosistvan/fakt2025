SELECT DISTINCT
	f1.veznev, f1.utonev
FROM 
	felhasznalo as f1
    JOIN felhasznalo as f2 on f1.veznev = f2.veznev 
    AND f1.utonev = f2.utonev
    AND f1.id <> f2.id
ORDER BY
	f1.veznev,
    f1.utonev;