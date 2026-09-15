SELECT
	m.nev as maszo_nev,
    c.nev as csucs_nev,
    c.magassag
FROM
	naplo as n
    join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
WHERE
	n.ev > 2000 AND c.orszag LIKE '%Kína%'
order by 
	c.magassag DESC;