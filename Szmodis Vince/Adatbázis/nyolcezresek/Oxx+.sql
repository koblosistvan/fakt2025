SELECT DISTINCT
	 m2.nev
    
FROM
	naplo as n1
    JOIN naplo as n2 on n1.csucsaz = n2.csucsaz and n1.ev = n2.ev
    
    JOIN maszo as m1 on n1.maszoaz = m1.az
    JOIN maszo as m2 on n2.maszoaz = m2.az
WHERE 
	n1.az != n2.az
    and m1.nev = 'Ugyan Anita';