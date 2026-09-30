SELECT
	c.nev,
    c.magassag
FROM
	naplo as n 
    join csucs as c on c.az = n.csucsaz
    join maszo as m on m.az = n.maszoaz
where 
	c.orszag NOT like "Kína" 
order by n.ev DESC
limit 3;