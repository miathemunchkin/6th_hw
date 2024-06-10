SELECT student.name, AVG(grade.value) 
FROM student
JOIN grade ON student.id = grade.student_id
GROUP BY student.id, student.name
ORDER BY AVG(grade.value) DESC
LIMIT 5
