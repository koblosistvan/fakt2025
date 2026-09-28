SELECT
	h.megnevezes,
    f.veznev,
    f.utonev,
    f.email
FROM
	felhasznalo as f
    join hirfolyam as h on h.id = f.id;