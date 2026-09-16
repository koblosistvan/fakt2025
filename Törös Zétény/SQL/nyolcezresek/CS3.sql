SELECT
	c.nev,
    count(*) as Expedicio_Száma
FROM 
	naplo as n 
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz
WHERE
	c.orszag LIKE "%Kína%"
GROUP BY
	c.az
ORDER BY
	count(*) DESC;