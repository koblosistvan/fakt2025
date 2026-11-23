SELECT DISTINCT
	t.nev
FROM
	tanar as t JOIN
    vizsgak as v ON v.tanarid = t.id
WHERE
	v.vizsgatargy = 'angol nyelv';