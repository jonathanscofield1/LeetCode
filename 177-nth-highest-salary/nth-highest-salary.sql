CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
     # Write your MySQL query statement below.
     select 
        salary 
     from(
        select 
            salary, 
            rank() 
            over w as r 
            from (
                select 
                distinct(salary) 
                from Employee) 
                as e window w as (order by salary desc)
            ) sub 
            where r = N
 );
END