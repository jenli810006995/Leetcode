* Time: Aug 29 2020

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

```
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```
The Department table holds all departments of the company.
```
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).
```
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```
Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

* Logic: Use left join for the Employee and the Department table, and be aware that to use group by DepartmentId can help us find the
highest salary within each department by later using max(salary). Also, left join would have the different result here than join.
We have to use join here.

* Solution:
```
select b.Name as Department, a.Name as Employee, a.Salary as Salary from Employee a
join Department b on a.DepartmentId = b.Id
where (a.Salary, a.DepartmentId) in
(select max(a.Salary), a.DepartmentId from Employee a
group by a.DepartmentId);

```

* [Link](https://leetcode.com/problems/department-highest-salary/)

