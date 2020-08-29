* Time: Aug. 25 2020

Write a SQL query to rank scores. If there is a tie between two scores, 
both should have the same ranking. Note that after a tie, 
the next ranking number should be the next consecutive integer value. 
In other words, there should be no "holes" between ranks.

```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```
For example, given the above Scores table, your query should generate the following report (order by highest score):
```
+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+
```
Important Note: For MySQL solutions, to escape reserved words used as column names, you can use an apostrophe before and after the keyword. For example `Rank`.

* Logic: count(distinct Score) + 1 as 'Rank'

* Solution

```
select Score as score,
(select count(distinct Score)+1 
from Scores a
where a.Score > b.Score) as 'Rank'
from Scores b
order by b.score desc;

```
* [Link](https://leetcode.com/problems/rank-scores/)