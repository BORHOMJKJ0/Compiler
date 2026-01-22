
SELECT * from EmployeeMaster WHERE salary IS NULL

SELECT * from EmployeeMaster WHERE employeename LIKE 'super'

SELECT * from EmployeeMaster WHERE employeename LIKE 'super''\\\\AZ\
c'

SELECT * from EmployeeMaster WHERE employeename LIKE 'super''\\\\AZ
c'

SELECT * from EmployeeMaster WHERE employeename LIKE 'sup%'

SELECT * from EmployeeMaster WHERE employeename LIKE '%man'

SELECT * from EmployeeMaster WHERE employeename NOT LIKE '%ra%'

/*will return 8 letter names starting with Su, containing p or j in between and ending in erman*/
SELECT * from EmployeeMaster WHERE employeename LIKE 'Su[pj]erman%'

/*will return 4 letter names starting with ra, containing n or j in between and ending in u*/
SELECT * from EmployeeMaster WHERE employeename LIKE 'ra[nj]u%'

/*will return 4 letter names starting with ra, NOT containing n or j in between and ending in u*/
SELECT * from EmployeeMaster WHERE employeename LIKE 'ra[^nj]u%'

SELECT * from EmployeeMaster WHERE employeename NOT LIKE 'raj%'

select * from EmployeeMaster WHERE EXISTS
(select * from EmployeeMaster where EmployeeName  LIKE 'superman')