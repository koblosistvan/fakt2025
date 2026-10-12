SELECT
	u.orszag,
    count(*) as orszag_urhajosai_szama
FROM
	urhajos as u
group BY
	u.orszag
order BY
	orszag_urhajosai_szama DESC