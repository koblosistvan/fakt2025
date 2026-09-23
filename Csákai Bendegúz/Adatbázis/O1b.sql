SELECT DISTINCT
    m1.nev
FROM
	csucs as c
	JOIN naplo as n1 on c.az = n1.csucsaz
    JOIN maszo as m1 on m1.az = n1.maszoaz
    JOIN naplo as n2 on c.az = n2.csucsaz
    JOIN maszo as m2 on m2.az = n2.maszoaz
WHERE
	m1.az <> m2.az
ORDER BY
	m1.nev;