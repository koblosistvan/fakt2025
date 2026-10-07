SELECT
	f.veznev,
    f.utonev,
    COUNT(*)
FROM
	felhasznalo as f 
    JOIN hirfolyam as h on h.moderator = f.id
    JOIN uzenet as u on u.f_id = f.id
WHERE
	h.megnevezes = 'e-bike'
    u.kuldido BETWEEN '12:00' and '16:00'
group by 
	uzenet