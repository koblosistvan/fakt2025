SELECT 
	c.nev,
    count(c.nev) as darab
FROM
	naplo as n
	join maszo as m on m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
WHERE
	c.orszag like '%Kína%'
GROUP BY
	n.csucsaz
ORDER BY
	darab desc;