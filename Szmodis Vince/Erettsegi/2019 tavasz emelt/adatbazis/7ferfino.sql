SELECT
	k.megnevezes
FROM
	urhajos as u 
    JOIN repules as r on r.urhajosid = u.id
    JOIN kuldetes as k on k.id = r.kuldetesid
GROUP BY
k.id
HAVING
	MAX(u.nem) = 'N' and MIN(u.nem) = 'F';