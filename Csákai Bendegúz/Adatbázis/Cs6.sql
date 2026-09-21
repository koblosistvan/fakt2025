SELECT 
	c.nev as csucs_nev,
    count(distinct m.az) as darab
FROM
	naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
GROUP BY
	c.az
HAVING
	darab > 1
ORDER BY
	darab DESC;