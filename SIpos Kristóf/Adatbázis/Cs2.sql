SELECT
	m.nev,
    c.magassag,
    max(c.magassag) as legnagyobb
from
	naplo as n
    join maszo as m on m.az = n.maszoaz
    join csucs as c on c.az = n.csucsaz
group BY
	m.nev
order by
	c.magassag DESC;