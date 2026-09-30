SELECT
	d.cim,
    m.nev
FROM
	darab_txt as d
    JOIN mufaj_txt as m on m.id = d.mufajid
WHERE
	d.cim like '%asszony%'
GROUP BY
	d.cim;