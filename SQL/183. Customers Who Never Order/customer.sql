SELECT NAME AS CUSTOMERS FROM CUSTOMERS
WHERE CUSTOMERS.ID NOT IN (SELECT CUSTOMER_ID FROM ORDERS_TABLE)

