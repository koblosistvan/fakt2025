SELECT 
	t.ev,
	g.vnev,
    t.csapat
FROM
	tour as t
    join gyoztesek as g on t.gyoztesid = g.vazon
WHERE
	g.vorszag = 'FRA'
order BY
	ev DESC
    LIMIT 1;
    