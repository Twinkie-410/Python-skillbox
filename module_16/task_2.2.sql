SELECT customer.full_name
    FROM `customer`
        LEFT OUTER JOIN `order` on `order`.customer_id = `customer`.customer_id
        WHERE `order`.customer_id IS NULL