SELECT
	f.veznev,
    f.utonev,
    u.tartalom,
    u.kuldido
from 
	uzenet as u
    join felhasznalo as f on f.id = u.f_id
    join hirfolyam as h on u.tartalom like concat('%', h.megnevezes,'%');