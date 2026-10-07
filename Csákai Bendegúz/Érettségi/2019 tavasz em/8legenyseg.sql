SELECT
	k.megnevezes as 'küldetés neve', k.kezdet as kezdete, u.nev as legénység, u.orszag as ország, u.nem
FROM
	repules as r
    JOIN urhajos as u on r.urhajosid = u.id
    JOIN kuldetes as k on r.kuldetesid = k.id
WHERE
	YEAR(k.kezdet) > 1990 AND
    YEAR(k.veg) < 2001
ORDER BY
	k.megnevezes,
	u.nev;
	
DE JELENTÉS NEM KELL