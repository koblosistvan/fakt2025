SELECT
	m.nev,
    n.ev,
    c.nev,
    c.magassag
FROM
	naplo as n 
    join maszo as m on n.maszoaz = m.az
    join csucs as c on n.csucsaz = c.az
WHERE 
	n.ev < 2000
ORDER BY
	m.nev,
    n.ev;