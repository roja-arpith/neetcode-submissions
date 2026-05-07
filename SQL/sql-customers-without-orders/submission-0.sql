-- Write your query below
-- select customer_id 
-- from customers
-- where year = 2020 and revenue > 0;

select c.name
from customers c 
left join orders o on c.id = o.customer_id
where o.customer_id is NULL;