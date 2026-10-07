SELECT
	t.ev, g.vnev, t.csapat
FROM
	tour as t
    JOIN gyoztesek as g on g.vazon = t.gyoztesid
WHERE
	g.vorszag = 'FRA'
ORDER BY
	t.ev DESC LIMIT 1;