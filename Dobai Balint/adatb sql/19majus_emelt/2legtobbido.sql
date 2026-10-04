SELECT
	u.nev,
    u.urido
FROM
	urhajos as u
WHERE
	u.nem = 'N'
order by u.urido desc limit 1;