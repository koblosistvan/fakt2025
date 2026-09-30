SELECT
	d.cim
FROM
	darab_txt as d
WHERE
	d.bemutato < 2001 AND
    d.utolso > 2001;