SELECT
	u.nev, u.urido
FROM
	urhajos as u
WHERE
	u.nem = 'N'
ORDER BY
	u.urido DESC LIMIT 1;