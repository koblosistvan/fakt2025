SELECT
	c.nev,
    count(distinct m.az) as Expedíciók
FROM 
	naplo as n 
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz
GROUP BY
	c.az
having
	count(distinct m.az)
ORDER by
	Expedíciók desc;