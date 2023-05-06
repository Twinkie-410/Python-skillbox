SELECT full_name, AVG(ag.grade) as avg_grade
    FROM students
    INNER JOIN assignments_grades ag on students.student_id = ag.student_id
    GROUP BY students.student_id
    ORDER BY avg_grade DESC
    LIMIT 10