SELECT
	k.megnevezes
FROM
	kuldetes as k
    JOIN repules as r on r.kuldetesid = k.id
    JOIN urhajos as u on u.id = r.urhajosid
HAVING
	COUNT(u.nem = 'N') > 0 and COUNT(u.nem = 'F') > 0