CREATE TABLE IF NOT EXISTS grade (
    id SERIAL NOT NULL,
    student_id INTEGER,
    subject_id INTEGER,
    value SMALLINT,
    date DATE,
    CONSTRAINT grade_PK PRIMARY key (id),
    CONSTRAINT grade_FK_student_id FOREIGN KEY(student_id) REFERENCES student(id),
    CONSTRAINT grade_FK_subject_id FOREIGN KEY(subject_id) REFERENCES subject(id)
);