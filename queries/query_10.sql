SELECT DISTINCT subject.name
FROM subject
JOIN grade ON subject.id = grade.subject_id
JOIN teacher ON teacher.id = subject.teacher_id  
WHERE grade.student_id = 33 and teacher.name = 'Megan Crawford'