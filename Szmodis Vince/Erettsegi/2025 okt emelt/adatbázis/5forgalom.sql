SELECT
	h.megnevezes,
    COUNT(*) as uzenetek_szama
FROM
	hirfolyam as h
    join uzenet as u on u.h_id = h.id
GROUP by 
	h.id;