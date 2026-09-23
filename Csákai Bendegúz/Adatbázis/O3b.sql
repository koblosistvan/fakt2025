SELECT 
	c.nev
FROM
	csucs as c
    
    JOIN naplo as n1 on c.az = n1.csucsaz
    JOIN naplo as n2 on c.az = n2.csucsaz

WHERE
	n1.ev = 2005 AND
   	n2.ev = 2009;

________________________________________
SELECT 
	csucs.nev
FROM
	csucs
WHERE
	az in (SELECT 
                n.csucsaz
            FROM
				naplo as n
            WHERE
                n.ev = 2005) AND
	az in (SELECT 
                n.csucsaz
            FROM
				naplo as n
            WHERE
                n.ev = 2009);