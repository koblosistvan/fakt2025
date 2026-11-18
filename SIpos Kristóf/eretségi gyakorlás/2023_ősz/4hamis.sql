SELECT
	sz.szinesz,
    sz.szerep
FROM
	stab as s
    JOIN film as f on s.filmid=f.id
    JOIN szereplo as sz on s.szereploid =s.id
WHERE
	f.cim = 'Hamis a baba'