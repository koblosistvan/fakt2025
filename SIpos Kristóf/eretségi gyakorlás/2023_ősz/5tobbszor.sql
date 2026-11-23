SELECT
	sz.szinesz,
    COUNT(*) as összes_szerep
FROM
	stab as s
    JOIN film as f on s.filmid=f.id
    JOIN szereplo as sz on s.szereploid =s.id
GROUP BY
	sz.szinesz
order by
	összes_szerep