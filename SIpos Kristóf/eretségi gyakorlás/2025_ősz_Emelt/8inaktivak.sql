SELECT
	f.veznev,
    f.utonev
FROM
	felhasznalo as f
    left join uzenet as u on u.f_id =f.id
WHERE
	f.utolso < '2010-01-01'
    and u.id is null;