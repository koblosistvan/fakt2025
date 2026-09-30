SELECT
	m.nev,
    c.nev,
    c.magassag
from naplo as n
	join csucs as c on c.az = n.csucsaz
    join maszo as m on m.az = n.maszoaz
where n.ev < 2000 or c.orszag like "%Pakisztán%"
order by m.nev desc , c.magassag;