CREATE TABLE IF NOT EXISTS student (
    id SERIAL NOT NULL,
    name VARCHAR(100) NOT NULL,
    group_id INTEGER,
    CONSTRAINT student_PK PRIMARY key (id),
    CONSTRAINT student_FK_group_id FOREIGN KEY(group_id) REFERENCES "group"(id)
);