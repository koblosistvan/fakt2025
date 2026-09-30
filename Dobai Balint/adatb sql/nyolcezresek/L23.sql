select
	m.nev,
    n.ev,
    c.nev,
    c.magassag
FROM
	naplo as n
    join maszo as m on m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
where 
	n.ev <2000
	order by m.nev desc, n.ev DESC;