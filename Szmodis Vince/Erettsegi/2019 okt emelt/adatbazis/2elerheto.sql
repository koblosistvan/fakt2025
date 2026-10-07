SELECT
	s.nev
FROM
	szemely as s 
WHERE
	s.elerheto = 'igaz'
ORDER BY
	s.nev