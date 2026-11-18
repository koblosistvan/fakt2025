SELECT
	a.nev, COUNT(*) as legtobb
FROM
	alkotok as a
   	JOIN filmstab as s on s.alkazon = a.alkotoazon
    JOIN filmek as f on s.fazon = f.filmazon
WHERE
	s.munkakor = 6
GROUP BY
	a.nev
ORDER BY
	legtobb desc LIMIT 1;