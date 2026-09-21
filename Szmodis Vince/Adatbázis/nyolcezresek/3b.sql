SELECT
	*
FROM
	csucs
WHERE
	az in(
            SELECT
            n.csucsaz
        FROM
            maszo as m 
            join naplo as n on n.maszoaz = m.az
        WHERE
            m.nev = 'Ugyan Anita'        
    )
    AND
    az in(SELECT
            n.csucsaz
        FROM
            maszo as m 
            join naplo as n on n.maszoaz = m.az
        WHERE
            m.nev = 'Erőss Zsolt'
          );