SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount  
FROM trainee  
FULL OUTER JOIN fee ON trainee.admission_no = fee.admission_no;