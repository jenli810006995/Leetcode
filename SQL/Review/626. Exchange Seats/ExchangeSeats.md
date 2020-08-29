* Time: Aug 29 2020

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?
 
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```
For the sample input, the output is:
 
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```
Note:
If the number of students is odd, there is no need to change the last one's seat.


* Logic: check if the id = cnt(aka the total number) and if the cnt is odd, then there is no need to change the seats
One thing to notice is that we have to create a temp table t to store the new id and student variables, and then order by id

* Solution:
```
select if(cnt%2=1 and id =cnt, id, if(id%2=1, id+1, id-1)) as id, student from seat,
(select count(*) as cnt from seat) as t
order by id;
```
* [link](https://leetcode.com/problems/exchange-seats/)

