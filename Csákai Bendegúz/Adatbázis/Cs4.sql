SELECT 
	c.nev as csucs_nev,
    count(*) as darab
FROM
	naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
WHERE
	m.ferfi = 0
GROUP BY
	c.az
ORDER BY
	darab DESC;