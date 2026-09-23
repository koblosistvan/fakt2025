SELECT
	n.ev,
    c.nev as csucs_nev,
    c.magassag
from 
	naplo as n
    JOIN maszo as m on m.az=n.maszoaz
    JOIN csucs as c on c.az=n.csucsaz
WHERE
	m.nev = 'Erőss Zsolt'
order BY
	ev;