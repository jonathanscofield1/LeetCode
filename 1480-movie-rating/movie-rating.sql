# Write your MySQL query statement below
select * from (select u.name as results from 
(select user_id, count(user_id) as total_rating from MovieRating group by user_id) as t left join users as u on t.user_id = u.user_id order by total_rating desc, u.name asc limit 1) as result1
UNION ALL
select * from (select title from (select title, avg(rating) as avg_rating from MovieRating r left join movies m on m.movie_id = r.movie_id where year(created_at) = 2020 and month(created_at) = 02 group by r.movie_id order by avg_rating desc, title asc limit 1) as agg) as result2
;







