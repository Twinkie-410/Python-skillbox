SELECT order_no, customer.full_name
    FROM `order`
        INNER JOIN `customer` on `customer`.customer_id = `order`.customer_id
        WHERE "order".manager_id IS NULL