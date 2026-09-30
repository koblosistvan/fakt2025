SELECT
	u.tartalom
FROM
	uzenet as u
WHERE
	u.tartalom LIKE '%bicikli%'
    OR u.tartalom LIKE '%bike%';