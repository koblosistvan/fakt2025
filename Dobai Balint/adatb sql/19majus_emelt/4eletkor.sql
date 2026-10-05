SELECT
	nev,
	MIN(YEAR(kezdet))-u.szulev as elso,
    MAX(YEAR(kezdet))-u.szulev as utolso    
    
FROM
	urhajos as u
    join repules as r on u.id = r.urhajosid 
    join kuldetes as k on k.id = r.kuldetesid 

group by u.id

having count(u.id) >1;