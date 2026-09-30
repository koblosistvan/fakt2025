SELECT
	h.megnevezes,
    count(*) as uzenetek_szama
from
	hirfolyam as h
	join uzenet as u on u.h_id = h.id
    
group by 
h.id
order by uzenetek_szama DESC;