SELECT
	sz.szinesz,
    count(*) as szerep_szam
FROM
	film as f 
    JOIN stab as s on s.filmid = f.id
    JOIN szereplo as sz on sz.id = s.szereploid
group by
	sz.szinesz
having
	count(*)>1;