SELECT
    m1.nev
FROM
	csucs as c 
    JOIN naplo as n1 on n1.csucsaz = c.az
    JOIN maszo as m1 on n1.maszoaz = m1.az
	JOIN naplo AS n2 on c.az = n2.csucsaz
    JOIN maszo as m2 on n2.maszoaz = m2.az
WHERE 
	m1.az != m2.az;