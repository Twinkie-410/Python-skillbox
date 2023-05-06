SELECT ag.assisgnment_id, round(avg(grade), 2) as avg_grade, assignment_text
    FROM assignments_grades as ag
    INNER JOIN (SELECT assisgnment_id, assignment_text
                    FROM assignments
                    WHERE assignment_text like 'прочитать%' or assignment_text like 'выучить%') as a
        ON a.assisgnment_id = ag.assisgnment_id
    GROUP BY a.assisgnment_id