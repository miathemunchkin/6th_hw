SELECT DISTINCT subject.name
FROM subject
JOIN grade ON subject.id = grade.subject_id
WHERE grade.student_id = 3