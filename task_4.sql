SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    COLUMN_KEY,
    EXTRA
FROM
    INFORMATION_SCHEMA,COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'Books';