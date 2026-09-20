SELECT 
	d.cim,
    m.nev
FROM
	darab as d
    JOIN mufaj as m ON d.mufajid = m.id
ORDER BY
	(d.utolso-d.bemutato) DESC
	LIMIT 1;