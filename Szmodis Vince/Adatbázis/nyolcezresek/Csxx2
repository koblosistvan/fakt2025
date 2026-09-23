SELECT
	m.nev,
    max(c.magassag)
FROM
	maszo as m
    join csucs as c on m.az = c.az
group by 
	m.az
	
order by 
	c.magassag DESC;