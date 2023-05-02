SELECT customer.full_name, manager.full_name, purchase_amount, date
    FROM `order`
        INNER JOIN `customer` on `customer`.customer_id = `order`.customer_id
        INNER JOIN `manager` on "order".manager_id = manager.manager_id