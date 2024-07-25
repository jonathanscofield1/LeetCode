-- Write your PostgreSQL query statement below
SELECT department.NAME AS "Department",
       employee.NAME   AS "Employee",
       salary          AS "Salary"
FROM   (SELECT Max(salary) AS max_sal,
               departmentid
        FROM   employee
        GROUP  BY departmentid) AS A
       LEFT JOIN employee
              ON employee.salary = A.max_sal
                 AND employee.departmentid = A.departmentid
       LEFT JOIN department
              ON department.id = employee.departmentid; 