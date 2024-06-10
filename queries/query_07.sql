SELECT student.name, grade.value
FROM student
JOIN grade ON student.id = grade.student_id
JOIN subject ON grade.subject_id = subject.id
JOIN "group" ON "group".id = student.group_id 
WHERE subject.name = 'subject1' and "group".name = 'group1' 
