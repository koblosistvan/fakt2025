SELECT
	sz.szinesz,
    sz.szerep
FROM
	film as f 
    JOIN stab as s on s.filmid = f.id
    JOIN szereplo as sz on sz.id = s.szereploid
group by 
	sz.id
having
	count(*)=7;