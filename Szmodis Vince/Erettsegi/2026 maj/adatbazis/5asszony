SELECT
	d.cim,
    m.nev
FROM
	darab as d
    join mufaj as m ON d.mufajid = m.id
WHERE
	d.cim like '%asszony%'
GROUP BY
	d.cim;