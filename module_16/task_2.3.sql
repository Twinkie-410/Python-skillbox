SELECT order_no, manager.full_name, customer.full_name
    FROM `order`
        INNER JOIN `customer` on `customer`.customer_id = `order`.customer_id
        INNER JOIN `manager` on "order".manager_id = manager.manager_id
        WHERE manager.city != customer.city