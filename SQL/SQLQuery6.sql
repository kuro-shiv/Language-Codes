CREATE TABLE Employee1 (
  EmpNo INT PRIMARY KEY,
  name VARCHAR(50),
  Salary DECIMAL(10,2),
  Age INT
);

INSERT INTO Employee1 (EmpNo, name, Salary, Age) VALUES
(1, 'Aarav', 50000.00, 25),
(2, 'Aditi', 60000.50, 30),
(3, 'Amit', 75000.75, 35),
(4, 'Anjali', 45000.25, 28),
(5, 'Chetan', 80000.00, 32),
(6, 'Divya', 65000.00, 27),
(7, 'Gaurav', 55000.50, 29),
(8, 'Isha', 72000.75, 31),
(9, 'Kavita', 48000.25, 26),
(10, 'Mohan', 83000.00, 33),
(11, 'Bharthy', 93000.00, 25),
(12, 'Saurabh', 40000.00, 35),
(13, 'Ankur', 70000.00, 40),
(14, 'Shraddha', 49000.00, 36),
(15, 'Gaurav', 90000.00, 25),
(16, 'Rohit', 89000.00, 26);



----find highest paid 3 emp
SELECT TOP 3 *
FROM Employee1
ORDER BY Salary DESC;



----emp earning more than avg salary
SELECT * 
FROM Employee1
WHERE Salary > (SELECT AVG(Salary) FROM Employee1);


-----COUNT EMP IN EACH AGE GROUP
SELECT Age, COUNT(*) AS EmployeeCount
FROM Employee1
GROUP BY Age
ORDER BY Age;


----CALCULATE TOTAL, AVG, MAXIMUM, MINIMUM SALARY
SELECT 
    SUM(Salary) AS TotalSalary,
    AVG(Salary) AS AverageSalary,
    MAX(Salary) AS MaximumSalary,
    MIN(Salary) AS MinimumSalary
FROM Employee1;



----FIND YOUNGEST AND OLDEST EMP
SELECT * 
FROM Employee1
WHERE Age = (SELECT MIN(Age) FROM Employee1)
   OR Age = (SELECT MAX(Age) FROM Employee1);



---COLUMN OF CITY 
ALTER TABLE Employee1
ADD City VARCHAR(50);



---ADD DATA OF CITY INSERT
UPDATE Employee1 SET City = 'Lucknow' WHERE EmpNo = 1;
UPDATE Employee1 SET City = 'Delhi' WHERE EmpNo = 2;
UPDATE Employee1 SET City = 'Mumbai' WHERE EmpNo = 3;
UPDATE Employee1 SET City = 'Pune' WHERE EmpNo = 4;
UPDATE Employee1 SET City = 'Chennai' WHERE EmpNo = 5;
UPDATE Employee1 SET City = 'Bangalore' WHERE EmpNo = 6;
UPDATE Employee1 SET City = 'Jaipur' WHERE EmpNo = 7;
UPDATE Employee1 SET City = 'Hyderabad' WHERE EmpNo = 8;
UPDATE Employee1 SET City = 'Indore' WHERE EmpNo = 9;
UPDATE Employee1 SET City = 'Bhopal' WHERE EmpNo = 10;
UPDATE Employee1 SET City = 'Varanasi' WHERE EmpNo = 11;
UPDATE Employee1 SET City = 'Patna' WHERE EmpNo = 12;
UPDATE Employee1 SET City = 'Ahmedabad' WHERE EmpNo = 13;
UPDATE Employee1 SET City = 'Kolkata' WHERE EmpNo = 14;
UPDATE Employee1 SET City = 'Noida' WHERE EmpNo = 15;
UPDATE Employee1 SET City = 'Gurgaon' WHERE EmpNo = 16;



----VERIFY TABLE
SELECT * FROM Employee1;


---



