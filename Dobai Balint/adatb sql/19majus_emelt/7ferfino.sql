SELECT
	k.megnevezes
FROM
	urhajos as u
    join repules as r on u.id = r.urhajosid 
    join kuldetes as k on k.id = r.kuldetesid 

group by k.id

HAVING
	min(u.nem) != max(u.nem);