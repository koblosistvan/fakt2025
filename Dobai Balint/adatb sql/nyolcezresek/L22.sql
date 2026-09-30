SELECT
	m.nev,
    n.ev,
    c.magassag,
    c.nev as csucs_nev
FROM
	naplo as n 
    join maszo as m ON m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
where n.ev = 2007
order by csucs_nev