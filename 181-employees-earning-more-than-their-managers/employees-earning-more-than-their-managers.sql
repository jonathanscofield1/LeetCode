/* Write your PL/SQL query statement below */
SELECT 
    e.name AS Employee
FROM
    Employee m LEFT JOIN Employee e ON m.id = e.managerId
WHERE
    e.salary > m.salary
;
