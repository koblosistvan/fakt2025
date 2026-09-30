SELECT
	h.megnevezes,
    f.veznev,
    f.utonev,
    f.email
FROM
	hirfolyam as h
    JOIN felhasznalo as f on f.id = h.moderator;