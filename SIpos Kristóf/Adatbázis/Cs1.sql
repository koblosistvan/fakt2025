SELECT
	m.nev,
    COUNT(*) AS darab
FROM
	naplo as n
    join maszo as m on m.az=n.maszoaz
GROUP by
	m.nev
order by
	m.nev
