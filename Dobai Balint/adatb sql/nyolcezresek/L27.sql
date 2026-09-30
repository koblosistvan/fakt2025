SELECT
	m.nev,
    n.ev,
    c.nev,
    c.magassag
from naplo as n
	join csucs as c on c.az = n.csucsaz
    join maszo as m on m.az = n.maszoaz
order by m.nev desc, c.magassag desc;