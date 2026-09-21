SELECT
	m.nev,
	n.ev,
    c.nev,
    c.magassag
FROM
    naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
WHERE
	n.ev < 2000
ORDER BY
	m.nev,
    n.ev;