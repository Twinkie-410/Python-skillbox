SELECT count_students,
       avg_grade,
       count_pass_students,
       count_overdue_students,
       sum(replay) as replay
    FROM(SELECT count(DISTINCT students.student_id) as count_students,
               count(DISTINCT students.student_id) - count(distinct ag.student_id) count_pass_students
            FROM students
            LEFT JOIN assignments_grades ag on students.student_id = ag.student_id)
    INNER JOIN (SELECT count(DISTINCT student_id) as count_overdue_students
            FROM assignments
            INNER JOIN assignments_grades ag on assignments.assisgnment_id = ag.assisgnment_id
            WHERE ag.date > assignments.due_date)
    INNER JOIN (SELECT round(avg(grade), 2) as avg_grade
                    FROM assignments_grades)
    INNER JOIN (SELECT assisgnment_id, (count(student_id) - count(DISTINCT student_id)) as replay
                FROM assignments_grades
                GROUP BY assisgnment_id
                HAVING count(student_id) > count(DISTINCT student_id)) as re_delivery