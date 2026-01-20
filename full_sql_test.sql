-- Single line comment
-- SELECT * FROM test;

 /*
   Multi line comment
   /* Nested comment */
   /* Nested comment */
   /* Nested comment */
   /* Nested comment */
   /* Nested comment */
  /*/* /* Nested comment */Nested comment */ Nested comment */
   /* Nested comment */
   /* Nested comment */
 */
CREATE TABLE dbo.[User Table] (
    user_id INT NOT NULL,
    userName NVARCHAR(100),
    "user-email" NVARCHAR(150),
    isActive BIT DEFAULT 1
);
