CREATE TABLE IF NOT EXISTS subject (
    id SERIAL NOT NULL,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER,
    CONSTRAINT subject_PK PRIMARY key (id),
    CONSTRAINT subject_FK_teacher_id FOREIGN KEY(teacher_id) REFERENCES teacher(id)
);