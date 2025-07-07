use SRMCEM;

CREATE TABLE Customer_records
(
CustomerID int primary key identity(1,1),
CustomerName varchar(50),
Contact varchar(50),
Address varchar(50),
City varchar(50),
PostalCode int,
Country varchar(50),
)

INSERT INTO Customer_records(CustomerName, Contact, Address, City, PostalCode, Country)
VALUES 
('Aarav Sharma', '9123456780', 'MG Road', 'Mumbai', 400001, 'India'),
('Ishita Verma', '9876543210', 'Sector 62', 'Noida', 201301, 'India'),
('Rohan Singh', '9988776655', 'Park Street', 'Kolkata', 700016, 'India'),
('Ananya Mishra', '9012345678', 'Ashok Nagar', 'Bhopal', 462001, 'India'),
('Kunal Patel', '9090909090', 'Lakeview Ave', 'Chicago', 60616, 'USA'),
('Meera Joshi', '9300001111', 'Oxford Street', 'London', 10115, 'UK'),
('Aditya Rao', '9321234567', 'Rue de Rivoli', 'Paris', 75001, 'France'),
('Sneha Kapoor', '9833445566', 'BTM Layout', 'Bengaluru', 560076, 'India'),
('Vikas Nair', '9445566778', 'Yonge Street', 'Toronto', 54545, 'Canada'),
('Divya Desai', '9870011223', 'Shibuya Crossing', 'Tokyo', 1500002, 'Japan'),
('Nikhil Gupta', '9098989898', 'Rajendra Nagar', 'Indore', 452012, 'India'),
('Pooja Yadav', '9811122233', 'Lalkothi', 'Jaipur', 302015, 'India'),
('Siddharth Jain', '9301234567', 'Kreuzberg', 'Berlin', 10997, 'Germany'),
('Ritika Malhotra', '9288776655', 'Sector 17', 'Chandigarh', 160017, 'India'),
('Yash Tripathi', '9223344556', 'Gomti Nagar', 'Lucknow', 226010, 'India'),
('Neha Saxena', '9871122334', 'Aliganj', 'Lucknow', 226024, 'India'),
('Manish Mehta', '9011223344', 'Manhattan', 'New York', 10001, 'USA'),
('Tanya Sahu', '9356677889', 'Sinsa-dong', 'Seoul', 06027, 'South Korea'),
('Rajeev Ranjan', '9778899001', 'Rajbansi Nagar', 'Patna', 800023, 'India'),
('Shruti Kulkarni', '9822446688', 'Shivaji Nagar', 'Pune', 411005, 'India'),
('Amitabh Rathi', '9988771122', 'CBD', 'Sydney', 2000, 'Australia'),
('Kavya Sehgal', '9812233445', 'Vesterbro', 'Copenhagen', 1620, 'Denmark'),
('Pranav Bhatt', '9344556677', 'Sheikh Zayed Rd', 'Dubai', '00000', 'UAE'),
('Simran Kaur', '9367889900', 'Phase 10', 'Mohali', 160062, 'India'),
('Rahul Tomar', '9887766554', 'Ginza', 'Tokyo', 1040061, 'Japan');


----for all data table view
select * from Customer_records


---find number of customer in each country

SELECT Country, COUNT(*) AS NumberOfCustomers
FROM Customer_records
GROUP BY Country
ORDER BY NumberOfCustomers DESC;


----find customer whose name start and  ends with vowel
SELECT * 
FROM Customer_records
WHERE 
    CustomerName LIKE '[AEIOUaeiou]%'  
    AND CustomerName LIKE '%[AEIOUaeiou]';  

----find customer whose country is india
SELECT * 
FROM Customer_records
WHERE Country = 'India';

----find customer whose contry is india and city is nodia
SELECT * 
FROM Customer_records
WHERE Country = 'India' AND City = 'Noida';


----customer have s
SELECT * FROM Customer_records	
WHERE CustomerName LIKE 'S%';


----top 3 cities
SELECT TOP 3 City, COUNT(*) AS CustomerCount
FROM Customer_records
GROUP BY City ORDER BY CustomerCount desc;

----duplicaate values
SELECT CustomerName, COUNT(*) AS DuplicateCount FROM Customer_records
GROUP BY CustomerName HAVING COUNT(*)>1;