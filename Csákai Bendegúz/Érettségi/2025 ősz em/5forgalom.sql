SELECT
	h.megnevezes, COUNT(u.tartalom) as uzenetek_szama
FROM 
	hirfolyam as h
    JOIN uzenet as u on u.h_id = h.id
GROUP BY
	u.h_id;