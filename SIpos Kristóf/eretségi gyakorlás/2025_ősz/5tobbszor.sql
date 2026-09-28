SELECT
	g.vnev,
   	count(*) as gyozelmek
FROM
    gyoztesek as g
    join tour as t on t.gyoztesid = g.vazon
group by
	(g.vnev)
HAVING
	gyozelmek > 1  
ORDER BY
	 gyozelmek Desc;