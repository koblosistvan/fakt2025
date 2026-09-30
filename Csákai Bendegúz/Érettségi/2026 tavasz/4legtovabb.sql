SELECT
	d.cim,
    m.nev
FROM
	darab_txt as d
    JOIN mufaj_txt as m on m.id = d.mufajid
HAVING
	MAX(d.utolso-d.bemutato);