SELECT
	*
FROM
	csucs

WHERE
	az in ( SELECT n.csucsaz FROM  naplo as n WHERE n.ev = 2005)
    and az in ( SELECT n.csucsaz FROM  naplo as n WHERE n.ev = 2009);