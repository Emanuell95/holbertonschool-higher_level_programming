-- Selecting the best score for each student
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;