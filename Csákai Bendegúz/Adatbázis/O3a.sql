SELECT	
	c.nev
FROM
	csucs as c
    
    JOIN naplo as n1 on c.az = n1.csucsaz
    JOIN maszo as m1 on m1.az = n1.maszoaz
    
    JOIN naplo as n2 on c.az = n2.csucsaz
    JOIN maszo as m2 on m2.az = n2.maszoaz

WHERE
	m1.nev = 'Ugyan Anita' and
    m2.nev = 'Erőss Zsolt';

________________________________________

SELECT 
	csucs.nev
FROM
	csucs
WHERE
	az in (SELECT 
                n.csucsaz
            FROM
                maszo as m
                JOIN naplo as n on m.az = n.maszoaz
            WHERE
                m.nev = 'Ugyan Anita') AND
	az in (SELECT 
                n.csucsaz
            FROM
                maszo as m
                JOIN naplo as n on m.az = n.maszoaz
            WHERE
                m.nev = 'Erőss Zsolt');