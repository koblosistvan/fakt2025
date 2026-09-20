SELECT
	m.nev as maszonev,
    c.magassag,
    c.nev,
    n.ev
FROM 
	naplo as n
    join maszo as m on n.maszoaz=m.az
    join csucs as c on n.csucsaz = c.az

WHERE
	n.ev=2007

ORDER BY
	magassag;