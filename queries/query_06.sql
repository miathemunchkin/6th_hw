SELECT student.name
FROM student 
JOIN "group" ON "group".id = student.group_id
WHERE "group".name = 'group1'  