CREATE TABLE Inventory (ID SERIAL PRIMARY KEY, UserId VARCHAR(50), Product VARCHAR(100), Quantity INT, CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE);
CREATE TABLE Users (UserId VARCHAR(50) PRIMARY KEY, HashedPassword VARCHAR(100), FirstName VARCHAR(50), LastName VARCHAR(50), Email VARCHAR(50));
CREATE TABLE UserHealth (UserId VARCHAR(50), Gender VARCHAR(25), UserHeight INT, UserWeight INT, UserAge INT, ActivityLevel VARCHAR(100), CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE);
CREATE TABLE PrescriptionItems (Medication VARCHAR(100), Dosage VARCHAR(100), PillCount INT, RefillDate DATE, ExpiryDate DATE, PillsUsedPerDay INT, UserId VARCHAR(50), CONSTRAINT fk_constraint FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE);

