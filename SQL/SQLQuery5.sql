Create table TestEmp
(
EmpId int,
EmpName varchar(50)
)



Create table TestEmpSal
(
EmpId int,
EmpSal numeric(10,2)
)


Insert into TestEmp(EmpId,EmpName) values (1,'Saurabh')
Insert into TestEmp(EmpId,EmpName) values (2,'Sanjay')
Insert into TestEmp(EmpId,EmpName) values (3,'Joe')
Insert into TestEmp(EmpId,EmpName) values (4,'Stefanie')
Insert into TestEmp(EmpId,EmpName) values (5,'Vinod')
Insert into TestEmp(EmpId,EmpName) values (9,'Vineet')

Select * from TestEmp


Insert into TestEmpSal(EmpId,EmpSal) values (1,10000)
Insert into TestEmpSal(EmpId,EmpSal) values (2,20000)
Insert into TestEmpSal(EmpId,EmpSal) values (4,30000)
Insert into TestEmpSal(EmpId,EmpSal) values (7,25000)
Insert into TestEmpSal(EmpId,EmpSal) values (8,35000)
Insert into TestEmpSal(EmpId,EmpSal) values (9,40000)


Select * from TestEmp
Select * from TestEmpSal



SELECT 
    E.EmpId,
    E.EmpName,
    S.EmpSal
FROM 
    TestEmp E
INNER JOIN 
    TestEmpSal S
ON 
    E.EmpId = S.EmpId;

SELECT 
    E.EmpId,
    E.EmpName,
    S.EmpSal
FROM 
    TestEmp E
FULL JOIN 
    TestEmpSal S
ON 
    E.EmpId = S.EmpId;


SELECT 
    E.EmpId,
    E.EmpName,
    S.EmpSal
FROM 
    TestEmp E
LEFT JOIN 
    TestEmpSal S
ON 
    E.EmpId = S.EmpId;

SELECT 
    E.EmpId,
    E.EmpName,
    S.EmpSal
FROM 
    TestEmp E
RIGHT JOIN 
    TestEmpSal S
ON 
    E.EmpId = S.EmpId;
