SELECT full_name
    FROM students
    INNER JOIN students_groups sg on students.group_id = sg.group_id
    INNER JOIN
        (SELECT teachers.teacher_id, AVG(ag.grade) as avg_grade
            FROM teachers
            INNER JOIN assignments a on teachers.teacher_id = a.teacher_id
            INNER JOIN assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
            GROUP BY full_name
            ORDER BY avg_grade DESC
            LIMIT 1) as chill_teacher
    WHERE sg.teacher_id = chill_teacher.teacher_id