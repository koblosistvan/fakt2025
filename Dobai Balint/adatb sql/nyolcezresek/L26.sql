SELECT
	m.nev,
    c.magassag,
    c.nev
FROM
	naplo as n 
    join csucs as c on c.az = n.csucsaz
    join maszo as m on m.az = n.maszoaz
where 
	c.orszag like "%Kína%" and
    n.ev > 2000
order by c.magassag;