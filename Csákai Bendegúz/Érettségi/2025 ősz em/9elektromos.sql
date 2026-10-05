SELECT
	f.veznev,
    f.utonev,
    count(u.tartalom) as uzenetek_szama
FROM
	felhasznalo as f
    JOIN uzenet as u on u.f_id = f.id
    JOIN hirfolyam as h on u.h_id = h.id
WHERE
	h.megnevezes = 'e-bike' and
    u.kuldido between '12:00:00' and '16:00:00'
GROUP BY
	u.f_id;