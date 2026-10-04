SELECT DISTINCT
f1.veznev,
f1.utonev
FROM
	felhasznalo as f1
    join felhasznalo as f2 
    on f1.veznev = f2.veznev
    and f1.utonev =f2.utonev
    and f1.id != f2.id;