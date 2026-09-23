SELECT
	m.nev,
    max(c.magassag) as Magasság
FROM 
	naplo as n 
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz
GROUP BY
	m.az
ORDER BY
	c.magassag DESC;