SELECT
	megnevezes,
    COUNT(*)
FROM 
	hirfolyam as h
    JOIN uzenet as u on u.h_id = h.id
GROUP BY
	h.id;