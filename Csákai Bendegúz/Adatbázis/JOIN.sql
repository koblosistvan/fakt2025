SELECT *
FROM
	naplo as n
    JOIN maszo as m on m.az = n.maszoaz
    JOIN csucs as c on c.az = n.csucsaz;