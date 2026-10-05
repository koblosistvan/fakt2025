SELECT
	u.tartalom
from
	uzenet as u
WHERE
	u.tartalom LIKE '%bicikli%' or  u.tartalom like '%bike%';