SELECT
	n.ev,
    c.nev,
    c.magassag
FROM
	naplo as n 
    join csucs as c on n.csucsaz = c.az
    JOIN maszo as m on n.maszoaz = m.az
WHERE
	m.nev = 'Erőss Zsolt'
ORDER BY
	n.ev;