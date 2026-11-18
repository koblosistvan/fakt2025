SELECT
	sz.szinesz,
    sz.szerep
from
	film as f 
    JOIN stab as s on s.filmid = f.id
    JOIN szereplo as sz on sz.id = s.szereploid
WHERE
	f.cim ='Hamis a baba';