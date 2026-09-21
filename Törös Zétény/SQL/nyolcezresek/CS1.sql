SELECT
	m.nev,
    count(*) as Expedicio_Száma
FROM 
	naplo as n 
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz
GROUP BY
	m.nev
ORDER BY
	m.nev;
