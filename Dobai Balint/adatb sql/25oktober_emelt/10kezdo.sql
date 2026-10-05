SELECT
	max(u.kuldido)
FROM
	uzenet as u
WHERE
	u.f_id = (select f_id from uzenet order by kuldido limit 1 );