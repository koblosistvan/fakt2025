SELECT
	m.nev,
    COUNT(*) as expediciokszama
FROM 
 	naplo as n
    JOIN maszo as m on n.maszoaz = m.az
GROUP by 
	m.az
HAVING
	COUNT(*) > 1;