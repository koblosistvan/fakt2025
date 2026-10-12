SELECT
	v.diaknev
FROM vizsgazo as v
	join vizsgak as vk on v.id = vk.vizsgazoid
group by diaknev
having count(*) >3;