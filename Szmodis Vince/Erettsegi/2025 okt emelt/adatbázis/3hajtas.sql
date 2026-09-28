SELECT
	u.tartalom
FROM
	uzenet as u
WHERE
	tartalom LIKE '%bicikli%' OR tartalom LIKE'%bike%';