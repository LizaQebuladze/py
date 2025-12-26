-- In 13.sql, write a SQL query to explore a question of your choice. This query should:
-- Involve at least one condition, using WHERE with AND or OR
SELECT strftime('%Y', air_date) AS year, COUNT(*) AS episode_count
FROM episodes
WHERE air_date BETWEEN '2002-01-01' AND '2007-12-31'
GROUP BY year
ORDER BY year;
--this query groups episodes by release data (between 2002 and 2007) and counts how many episodes were released each year and orders result by year


