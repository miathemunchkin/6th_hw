SELECT "group".name, AVG(grade.value)
FROM grade
JOIN subject ON subject.id = grade.subject_id
JOIN student ON student.id = grade.student_id
JOIN "group" ON "group".id = student.group_id
WHERE subject.name = 'subject2'
GROUP BY "group".id, "group".name 