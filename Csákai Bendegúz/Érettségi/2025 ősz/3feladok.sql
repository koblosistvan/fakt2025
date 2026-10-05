SELECT
	t.ev, t.tav, t.feladok/t.indulok as feladasok_aranya
FROM
	tour as t
ORDER BY
	feladasok_aranya DESC;