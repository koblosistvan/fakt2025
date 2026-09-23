SELECT
	m.nev,
    c.nev,
    c.magassag
FROM
    naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
WHERE
	c.orszag like '%Kína%' and
    n.ev > 2000
ORDER BY
	c.magassag DESC;