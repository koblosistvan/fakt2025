SELECT
	m.nev as maszo_nev,
    n.ev,
    c.nev as csucs_nev,
    c.magassag
FROM
    naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
ORDER BY
    n.ev,
	m.nev;