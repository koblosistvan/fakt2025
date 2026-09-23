SELECT
	c.nev as csucs_nev,
    n1.ev,
    m1.nev,
    n2.ev,
    m2.nev
from 
	csucs as c
   	join naplo as n1 on c.az =n1.csucsaz
    join maszo AS m1 on m1.az = n1.csucsaz
  
    JOIN naplo as n2 on c.az = n2.csucsaz
    JOIN maszo as m2 on m2.az = n2.maszoaz
where 
	m1.az != m2.az
order BY
	1;