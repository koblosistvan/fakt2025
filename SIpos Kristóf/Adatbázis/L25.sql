SELECT
	c.nev as csucs_nev,
    c.magassag
FROM
	naplo as n
    join maszo as m on m.az=n.maszoaz
    join csucs as c on c.az=n.csucsaz
WHERE
	c.orszag NOT LIKE 'kína'
order by
	n.ev DESC
    limit 3;