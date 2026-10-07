SELECT
	f.veznev,
    f.utonev,
    COUNT(*)
FROM
	uzenet as u 
    join felhasznalo as f on f.id = u.f_id
    JOIN hirfolyam as h on h.id = u.h_id
WHERE
	h.megnevezes = 'e-bike' AND
    u.kuldido BETWEEN '12:00:00' and '16:00:00'
group by 
	f.id;