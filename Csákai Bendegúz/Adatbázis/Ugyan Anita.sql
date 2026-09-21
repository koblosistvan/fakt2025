SELECT DISTINCT
    m2.nev
FROM
	naplo as n1
    join naplo as n2 on n1.csucsaz = n2.csucsaz and n1.ev = n2.ev
	
    JOIN maszo as m1 on m1.az = n1.maszoaz
	JOIN maszo as m2 on m2.az = n2.maszoaz 
WHERE
	n1.az <> n2.az
    and m1.nev = 'Ugyan Anita';