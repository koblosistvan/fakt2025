SELECT
	MAX(u.kuldido) as utolsó_üzenet
FROM
	uzenet as u 
where
	u.f_id =(
        SELECT 
        	f_id
        FROM
        	uzenet
        order BY
        	kuldido
        	limit 1
        );