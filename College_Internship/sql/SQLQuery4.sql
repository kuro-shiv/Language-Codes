create table EmployeeManager
(
EmployeeID int,
FirstName varchar(50),
LastName varchar(50),
ManagerID int,
)

Insert into EmployeeManager values(4529, 'Nancy', 'Young',4125)
Insert into EmployeeManager values(4238, 'John', 'Simon',4329)
Insert into EmployeeManager values(4329, 'Mafalda', 'Candreva',4125)
Insert into EmployeeManager values(4009, 'Klaus', 'Koch',4329)
Insert into EmployeeManager values(4125, 'Mafalda', 'Ranieri',null)
Insert into EmployeeManager values(4500, 'Jakub', 'Hrabal',4529)
Insert into EmployeeManager values(4118, 'Moira', 'Areas',4952)
Insert into EmployeeManager values(4012, 'Jon', 'Nilssen',4952)
Insert into EmployeeManager values(4952, 'Sandra', 'Rajkovic',4529)
Insert into EmployeeManager values(4444, 'Seamus', 'Quinn',4329)

select * from EmployeeManager

select ManagerID, count(*) as EmployeeCount
from EmployeeManager
where ManagerID is not null
group by ManagerID


---inner join for employee in each manager
SELECT 
    E.EmployeeID,
    E.FirstName AS EmployeeFirstName,
    E.LastName AS EmployeeLastName,
    M.EmployeeID AS ManagerID,
    M.FirstName AS ManagerFirstName,
    M.LastName AS ManagerLastName
FROM 
    EmployeeManager E
INNER JOIN 
    EmployeeManager M
ON 
    E.ManagerID = M.EmployeeID;


