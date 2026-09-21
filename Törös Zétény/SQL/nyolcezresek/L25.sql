SELECT
    c.nev,
    c.magassag
FROM
	naplo as n
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz
WHERE
	c.orszag not like '%Kína%'
ORDER BY
    n.ev DESC
LIMIT 3;