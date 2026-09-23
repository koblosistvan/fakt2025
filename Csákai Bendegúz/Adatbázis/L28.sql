SELECT
	m.nev as maszo_nev,
    c.nev as csucs_nev,
    c.magassag
FROM
    naplo as n
    JOIN csucs as c on c.az = n.csucsaz
    JOIN maszo as m on m.az = n.maszoaz
WHERE
	n.ev < 2000 OR c.orszag like '%Pakisztán%'
ORDER BY
    c.magassag,
	m.nev;