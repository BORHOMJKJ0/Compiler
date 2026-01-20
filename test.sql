/* ============================================================
   1. COMMENTS (Single & Multi + Nested)
   ============================================================ */

-- Single line comment
-- SELECT * FROM test;

 /*
   Multi line comment
   /* Nested comment */
 */

DECLARE @comment AS VARCHAR(20);
GO
/*
SELECT @comment = '/*';
*/ */
SELECT @@VERSION AS [Version];
GO


/* ============================================================
   2. IDENTIFIERS (normal, quoted, bracketed)
   ============================================================ */

CREATE TABLE dbo.[User Table] (
    user_id INT NOT NULL,
    userName NVARCHAR(100),
    "user-email" NVARCHAR(150),
    isActive BIT DEFAULT 1
);


/* ============================================================
   3. NUMBERS (int, float, scientific, negative)
   ============================================================ */

SELECT 0, 1, -5, 2147483647;
SELECT 3.14, -0.001, 1E10, 2.5e-3;


/* ============================================================
   4. BOOLEAN
   ============================================================ */

SELECT 1 WHERE 1 = 1;
SELECT 1 WHERE 1 <> 0;


/* ============================================================
   5. STRINGS (normal, escaped, multiline, binary, hex)
   ============================================================ */

SELECT 'Hello World';
SELECT 'It''s a beautiful day' AS Value;

-- Multiline string
SELECT 'abc\
def' AS ColumnResult;

-- Binary / Hex
SELECT 0xABCDEF;
SELECT 0xabc\
def AS BinaryResult;


/* ============================================================
   6. VARIABLES (User + System)
   ============================================================ */

DECLARE @x INT = 5;
DECLARE @y FLOAT;
SET @y = @x * 2.5;

SELECT @x, @y, @@VERSION;


/* ============================================================
   7. OPERATORS (Arithmetic, Logical, Bitwise, Comparison)
   ============================================================ */

SELECT 5 + 3 * 2;
SELECT (5 + 3) * 2;
SELECT 10 / 2, 10 % 3;

SELECT 1 & 0, 1 | 0, 1 ^ 1;

SELECT * FROM dbo.[User Table]
WHERE user_id >= 10 AND isActive = 1 OR userName IS NOT NULL;


/* ============================================================
   8. DDL STATEMENTS
   ============================================================ */

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    price DECIMAL(10,2),
    created_at DATETIME DEFAULT GETDATE()
);

ALTER TABLE Orders ADD status NVARCHAR(20);
DROP TABLE IF EXISTS Orders;


/* ============================================================
   9. DML STATEMENTS
   ============================================================ */

INSERT INTO dbo.[User Table] (user_id, userName)
VALUES (1, 'Ali'), (2, 'Sara');

UPDATE dbo.[User Table]
SET userName = 'Updated Name'
WHERE user_id = 1;

DELETE FROM dbo.[User Table]
WHERE user_id = 2;


/* ============================================================
   10. SELECT (basic → advanced)
   ============================================================ */

SELECT * FROM dbo.[User Table];

SELECT user_id, userName
FROM dbo.[User Table]
WHERE user_id IN (1,2,3)
ORDER BY userName DESC;

SELECT COUNT(*), isActive
FROM dbo.[User Table]
GROUP BY isActive
HAVING COUNT(*) > 0;


/* ============================================================
   11. JOINs
   ============================================================ */

SELECT u.userName, o.price
FROM dbo.[User Table] u
INNER JOIN Orders o ON u.user_id = o.user_id;

SELECT *
FROM dbo.[User Table] u
LEFT JOIN Orders o ON u.user_id = o.user_id;


/* ============================================================
   12. CASE / BETWEEN / EXISTS
   ============================================================ */

SELECT userName,
       CASE
           WHEN isActive = 1 THEN 'ACTIVE'
           ELSE 'INACTIVE'
       END AS status
FROM dbo.[User Table];

SELECT * FROM Orders
WHERE price BETWEEN 10 AND 100;

SELECT * FROM dbo.[User Table] u
WHERE EXISTS (
    SELECT 1 FROM Orders o WHERE o.user_id = u.user_id
);


/* ============================================================
   13. CTE (WITH)
   ============================================================ */

WITH ActiveUsers AS (
    SELECT user_id, userName
    FROM dbo.[User Table]
    WHERE isActive = 1
)
SELECT * FROM ActiveUsers;


/* ============================================================
   14. FUNCTIONS
   ============================================================ */

SELECT GETDATE(), LEN(userName), UPPER(userName)
FROM dbo.[User Table];


/* ============================================================
   15. CURSOR (basic)
   ============================================================ */

DECLARE user_cursor CURSOR FOR
SELECT user_id FROM dbo.[User Table];

OPEN user_cursor;
FETCH NEXT FROM user_cursor;
CLOSE user_cursor;
DEALLOCATE user_cursor;


/* ============================================================
   16. ERROR-PRONE / EDGE CASES
   ============================================================ */

SELECT;
SELECT FROM;
SELECT * FROM;

-- weird spacing
SELECT    *     FROM     dbo.[User Table];

-- multiple semicolons
SELECT 1;;;;;

