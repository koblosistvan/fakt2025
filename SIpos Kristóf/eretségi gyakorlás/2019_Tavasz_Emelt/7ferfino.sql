SELECT 
	k.megnevezes
FROM
	kuldetes as k
    JOIN repules as r on r.kuldetesid = k.id
    join urhajos as u on u.id = r.urhajosid
GROUP BY
	k.megnevezes
HAVING
	MAX(u.nem) != min(u.nem);