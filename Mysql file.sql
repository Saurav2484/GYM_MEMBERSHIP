CREATE DATABASE gym_management;

USE gym_management;

-- Members table
CREATE TABLE Members (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    DateOfBirth DATE,
    ContactNumber VARCHAR(15),
    Email VARCHAR(50),
    Address VARCHAR(100)
);

select * from members;
-- MembershipPlans table
CREATE TABLE MembershipPlans (
    PlanID INT PRIMARY KEY AUTO_INCREMENT,
    PlanName VARCHAR(50),
    Description VARCHAR(255),
    Duration INT,
    Price DECIMAL(8, 2)
);

select * from membershipPlans;
-- Add Member stored procedure
DELIMITER //
CREATE PROCEDURE AddMember(
    IN p_FirstName VARCHAR(50),
    IN p_LastName VARCHAR(50),
    IN p_Gender VARCHAR(10),
    IN p_DateOfBirth DATE,
    IN p_ContactNumber VARCHAR(15),
    IN p_Email VARCHAR(50),
    IN p_Address VARCHAR(100)
)
BEGIN
    INSERT INTO Members (FirstName, LastName, Gender, DateOfBirth, ContactNumber, Email, Address)
    VALUES (p_FirstName, p_LastName, p_Gender, p_DateOfBirth, p_ContactNumber, p_Email, p_Address);
END;,/
//
DELIMITER ;

-- Delete Member stored procedure
DELIMITER //
CREATE PROCEDURE DeleteMember(IN p_MemberID INT)
BEGIN
    DELETE FROM Members WHERE MemberID = p_MemberID;
END;
//
DELIMITER ;

-- Add Membership Plan stored procedure
DELIMITER //
CREATE PROCEDURE AddMembershipPlan(
    IN p_PlanName VARCHAR(50),
    IN p_Description VARCHAR(255),
    IN p_Duration INT,
    IN p_Price DECIMAL(8, 2)
)
BEGIN
    INSERT INTO MembershipPlans (PlanName, Description, Duration, Price)
    VALUES (p_PlanName, p_Description, p_Duration, p_Price);
END;
//
DELIMITER ;

-- Delete Membership Plan stored procedure
DELIMITER //
CREATE PROCEDURE DeleteMembershipPlan(IN p_PlanID INT)
BEGIN
    DELETE FROM MembershipPlans WHERE PlanID = p_PlanID;
END;
//
DELIMITER ;

-- Memberships table
CREATE TABLE Memberships (
    MembershipID INT PRIMARY KEY AUTO_INCREMENT,
    MemberID INT,
    PlanID INT,
    StartDate DATE,
    EndDate DATE,
    RenewalDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (PlanID) REFERENCES MembershipPlans(PlanID)
);

select * from Memberships;

-- Add Membership stored procedure
DELIMITER //
CREATE PROCEDURE AddMembership(
    IN p_MemberID INT,
    IN p_PlanID INT,
    IN p_StartDate DATE,
    IN p_EndDate DATE,
    IN p_RenewalDate DATE
)
BEGIN
    INSERT INTO Memberships (MemberID, PlanID, StartDate, EndDate, RenewalDate)
    VALUES (p_MemberID, p_PlanID, p_StartDate, p_EndDate, p_RenewalDate);
END;
//
DELIMITER ;

-- Delete Membership stored procedure
DELIMITER //
CREATE PROCEDURE DeleteMembership(IN p_MembershipID INT)
BEGIN
    DELETE FROM Memberships WHERE MembershipID = p_MembershipID;
END;
//
DELIMITER ;
