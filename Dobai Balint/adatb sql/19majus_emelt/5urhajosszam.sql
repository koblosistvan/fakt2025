SELECT
	u.orszag,
    count(u.nev) as urhajosok_szama
from urhajos as u

group by u.orszag

order by urhajosok_szama DESC;