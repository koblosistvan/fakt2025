SELECT
	MAX(u.kuldido)
FROM
	uzenet as u
WHERE
	u.f_id = (SELECT f_id FROM uzenet ORDER BY kuldido LIMIT 1 );