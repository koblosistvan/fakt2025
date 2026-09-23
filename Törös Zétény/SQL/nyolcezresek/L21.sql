SELECT 
	m.nev, 
	n.ev, 
    c.nev, 
	c.magassag
FROM 
	naplo as n 
    JOIN maszo as m on m.az = n.maszoaz 
    join csucs as c on c.az = n.csucsaz
ORDER BY ev;