SELECT
	m.nev,
    n.ev,
    c.nev,
    c.magassag
FROM
	naplo as n 
    join maszo as m ON m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
order by ev;