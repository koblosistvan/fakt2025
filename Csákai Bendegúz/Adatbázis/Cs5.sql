SELECT 
	m.nev as maszo_nev,
    count(*) as darab
FROM
	naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
GROUP BY
	m.az
ORDER BY
	darab DESC limit 3;