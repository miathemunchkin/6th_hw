SELECT student.name, AVG(grade.value) 
FROM student
JOIN grade ON student.id = grade.student_id
JOIN subject ON subject.id = grade.subject_id
WHERE subject.name = 'subject2'
GROUP BY student.id, student.name
ORDER BY AVG(grade.value) DESC
LIMIT 1