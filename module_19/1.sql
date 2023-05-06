SELECT full_name, AVG(ag.grade) as avg_grade
    FROM teachers
    INNER JOIN assignments a on teachers.teacher_id = a.teacher_id
    INNER JOIN assignments_grades ag on a.assisgnment_id = ag.assisgnment_id
    GROUP BY full_name
    ORDER BY avg_grade
    LIMIT 1