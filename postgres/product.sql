CREATE TABLE product AS

WITH master_data AS (
    SELECT
        arr->>'id' AS id,
        arr->>'type' AS type,
        arr->>'name' AS name,
        CAST(arr->>'ppu' AS FLOAT) AS ppu,
        (arr->>'batters')::JSON->>'batter' AS batter,
        arr->>'topping' AS topping
    FROM
        JSON_ARRAY_ELEMENTS('[{"id":"0001","type":"donut","name":"Cake","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1002","type":"Chocolate"},{"id":"1003","type":"Blueberry"},{"id":"1004","type":"Devil''s Food"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5007","type":"Powdered Sugar"},{"id":"5006","type":"Chocolate with Sprinkles"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]},{"id":"0002","type":"donut","name":"Raised","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]},{"id":"0003","type":"donut","name":"Old Fashioned","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1002","type":"Chocolate"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]}]'::JSON) AS arr
),

batter_data AS (
    SELECT
        id,
        batter->>'id' AS batter_id,
        batter->>'type' AS batter_type
    FROM
        (SELECT
            id,
            JSON_ARRAY_ELEMENTS(batter::JSON)::JSON AS batter
        FROM
            master_data) AS bat
),

topping_data AS (
    SELECT
        id,
        topping->>'id' AS topping_id,
        topping->>'type' AS topping_type
    FROM
        (SELECT
            id,
            JSON_ARRAY_ELEMENTS(topping::JSON)::JSON AS topping
        FROM
            master_data) AS top
)

SELECT
    md.id,
    md.type,
    md.name,
    md.ppu,
    bd.batter_id,
    bd.batter_type,
    td.topping_id,
    td.topping_type
FROM
    master_data AS md
LEFT JOIN
    batter_data AS bd
ON
    md.id = bd.id
LEFT JOIN
    topping_data AS td
ON
    md.id = td.id
