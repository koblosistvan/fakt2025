SELECT 
	m.nev,
    max(c.magassag)
FROM
	naplo as n
	join maszo as m on m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
GROUP BY
	m.az
ORDER BY
	c.magassag desc;