SELECT
	m.nev as maszo_nev,
    n.ev,
    c.nev as csucs_nev,
    c.magassag
FROM
	naplo as n
    join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
ORDER BY
	n.ev,m.nev