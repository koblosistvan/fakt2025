SELECT
	*
FROM
	csucs as c
    join naplo as n1 on n1.csucsaz=c.az
    join maszo as m1 on m1.az=n1.maszoaz

	join naplo as n2 on n2.csucsaz=c.az
    join maszo as m2 on m2.az= n2.maszoaz
WHERE
	m1.nev='Ugyan Anita'
    and m2.nev='Erőss Zsolt';