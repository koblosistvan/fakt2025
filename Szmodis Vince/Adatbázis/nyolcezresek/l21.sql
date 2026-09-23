SELECT
	m.nev as maszonev,
    n.ev,
    c.nev as csucsnev,
    c.magassag
FROM
	naplo as n 
    join maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az= n.csucsaz
ORDER BY
	ev;