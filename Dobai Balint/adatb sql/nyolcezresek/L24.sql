SELECT
	n.ev,
    c.nev,
    c.magassag
from naplo as n 
	join maszo as m on m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
where
	m.nev = 'Erőss Zsolt'
order by ev;