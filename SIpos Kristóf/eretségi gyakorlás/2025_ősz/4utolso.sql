SELECT 
	t.ev,
	g.vnev,
    t.csapat
FROM
	tour as t
    join gyoztesek as g
WHERE
	g.vorszag = 'FRA'
    