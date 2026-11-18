SELECT DISTINCT
	t.nev
FROM
	tanar as t
    JOIN vizsgak on vizsgak.tanarid = t.id
WHERE
	vizsgak.vizsgatargy = 'angol nyelv';