SELECT
	f.veznev,
    f.utonev,
    count(*) as uzenetek_szama
FROM
	uzenet as u
    JOIN felhasznalo as f on f.id = u.f_id
    join hirfolyam as h on h.id = u.h_id
WHERE
	h.megnevezes = 'e-bike'
    and u.kuldido between '12:00:00' and '16:00:00'
group by 
	f.id;