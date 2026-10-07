SELECT
	k.megnevezes
FROM
	kuldetes as k
	JOIN repules as r on r.kuldetesid = k.id
    JOIN urhajos as u on r.urhajosid = u.id
GROUP BY
	r.kuldetesid
HAVING
    MIN(u.nem) <> MAX(u.nem)