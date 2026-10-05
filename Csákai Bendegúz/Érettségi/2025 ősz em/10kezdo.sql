SELECT
	max(uzenet.kuldido)
FROM	
	uzenet
WHERE
	uzenet.f_id = (SELECT u.f_id FROM uzenet as u ORDER BY u.kuldido LIMIT 1);