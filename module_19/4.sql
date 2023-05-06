SELECT group_id,
       COUNT(assisgnment_id) as count_overdue_tasks,
       ROUND(AVG(overdue_tasks_count)) as avg_overdue,
       MAX(overdue_tasks_count) max_overdue,
       MIN(overdue_tasks_count) min_overdue
    FROM(
        SELECT group_id, assignments.assisgnment_id, SUM(assignments_grades.date > assignments.due_date) as overdue_tasks_count
        From assignments
        INNER JOIN assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
        GROUP BY assignments.assisgnment_id
        )
    GROUP BY group_id