SELECT
	u.tartalom
FROM
	uzenet as u
WHERE
	u.tartalom like '%bike%' OR
    u.tartalom like '%bicikli%';