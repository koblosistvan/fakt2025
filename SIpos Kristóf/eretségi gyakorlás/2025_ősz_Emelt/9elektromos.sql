SELECT
	f.veznev,
    f.utonev,
    COUNT(*) as uzenetek_szama
FROM
	felhasznalo as f
    join uzenet as u on u.f_id =f.id
    join hirfolyam as h on h.id = u.h_id
WHERE
	h.megnevezes = 'e-bike'
    and u.kuldido BETWEEN '12:00:00' AND '16:00:00'
GROUP BY
	f.id