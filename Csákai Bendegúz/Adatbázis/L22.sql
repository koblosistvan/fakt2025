SELECT
	m.nev as maszo_nev,
    n.ev,
    c.nev as csucs_nev,
    c.magassag
FROM
	naplo AS n
    JOIN maszo AS m on m.az = n.maszoaz
    JOIN csucs AS c on c.az = n.csucsaz
WHERE
	n.ev = 2007
ORDER BY
	c.nev;