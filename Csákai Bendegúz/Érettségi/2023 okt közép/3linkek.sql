SELECT
	f.cim, a.nev, f.ev, CONCAT('https://videotorium.hu/hu/recordings/',f.filmazon) as webcim
FROM
	filmek as f
    JOIN filmstab as s on f.filmazon = s.fazon
    JOIN alkotok as a on a.alkotoazon = s.alkazon
WHERE
	s.munkakor = 1;