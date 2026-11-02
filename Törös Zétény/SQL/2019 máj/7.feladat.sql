SELECT
	k.megnevezes,
    k.kezdet,
    u.nev
FROM
	kuldetes as k
    JOIN repules as r on r.kuldetesid = k.id
    JOIN urhajos as u on r.urhajosid = u.id
WHERE
	year(k.kezdet) BETWEEN 1991 and 2000
ORDER BY
	u.nev;