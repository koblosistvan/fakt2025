SELECT
	a.nev
FROM
	alkotok as a
	JOIN filmstab as s on s.alkazon = a.alkotoazon
    JOIN filmek as f on f.filmazon = s.fazon
WHERE
	f.cim = 'Mephisto' AND
	a.elhunyt IS NULL AND
    (s.munkakor = 1 OR s.munkakor = 6);