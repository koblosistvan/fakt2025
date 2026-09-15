SELECT
	m.nev,
    c.nev,
    c.magassag
FROM
	naplo as n 
    JOIN maszo as m on n.maszoaz = m.az
    JOIN csucs as c on n.csucsaz = c.az
WHERE
	c.orszag LIKE '%kína%'
ORDER by 
	c.magassag DESC;