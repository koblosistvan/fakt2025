SELECT 
	m.nev,
    count(*) as expediciok_szama
FROM
	naplo as n
	join maszo as m on m.az = n.maszoaz
WHERE 
	n.ev > 2000
GROUP BY
	m.az
having    
	count(*) > 1;