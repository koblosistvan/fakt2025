SELECT
	DISTINCT t.nev
FROM vizsgak as vk
join tanar as t on t.id = vk.tanarid
WHERE
	vk.vizsgatargy = "angol nyelv";