SELECT DISTINCT(E1.EMAIL) AS EMAIL FROM PERSON E1, PERSON E2 
WHERE E1.EMAIL  = E2.EMAIL AND E1.ID <> E2.ID

