-- In 8.sql, write a query that counts the number of episodes released in the last 6 years, from 2018 to 2023, inclusive.
-- You might find it helpful to know you can use BETWEEN with dates, such as BETWEEN '2000-01-01' AND '2000-12-31'.
SELECT COUNT(*)
FROM episodes
WHERE air_date BETWEEN '2018-01-01' AND '2023-12-31'; -- count episodes from 2018 to 2023

--but it says "episodes released in the last 6 years" so it should be from 2020 to 2025(even though in db there is no data for 2024 and 2025)
SELECT COUNT(*)
FROM episodes
WHERE air_date BETWEEN '2020-01-01' AND '2025-12-31';

