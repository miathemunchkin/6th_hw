SELECT AVG(grade.value), subject.name
FROM grade 
JOIN subject ON grade.subject_id = subject.id
WHERE subject.teacher_id = 15
GROUP BY subject.name 