CREATE TABLE Users (
    EmailId varchar(255) NOT NULL,
    UserName varchar(255) NOT NULL,
    PRIMARY KEY (EmailId)
);

CREATE TABLE Challenges (
    Id int NOT NULL IDENTITY(1, 1),
    Title varchar(255) NOT NULL,
    Description VARCHAR(8000) NULL,
    ImageUrl varchar(512) NULL,
    CreatorId varchar(255),
    CreatedDate date NOT NULL,
    EndDate date NULL,
    Active BIT NOT NULL,
    Badge NVARCHAR(100) NOT NULL,
    PRIMARY KEY (Id),
    CONSTRAINT FK_UserChallenge FOREIGN KEY (CreatorId) REFERENCES Users(EmailId) ON DELETE CASCADE
);

CREATE TABLE ChallengesAccepted (
    Id int NOT NULL IDENTITY(1, 1),
    UserId varchar(255) NOT NULL,
    ChallengeId int NOT NULL,
    Completed BIT NOT NULL,
    PhotoUrl varchar(MAX),
    Comment varchar(255),
    Reward NVARCHAR(100) NULL,
    PRIMARY KEY (Id),
    CONSTRAINT FK_UserChallengeAccepted FOREIGN KEY (UserId) REFERENCES Users(EmailId),
    CONSTRAINT FK_ChallengeChallengeAccepted FOREIGN KEY (ChallengeId) REFERENCES Challenges(Id) ON DELETE CASCADE
);

CREATE TABLE Badges (
badge NVARCHAR(100) NOT NULL, 
PRIMARY KEY (badge)
)


-- ALTER TABLE Challenges
-- ADD Badge NVARCHAR(100);

-- ALTER TABLE ChallengesAccepted
-- ALTER COLUMN reward NVARCHAR(100);

-- ALTER TABLE Challenges
-- ALTER COLUMN Description VARCHAR(8000) NULL

ALTER TABLE Challenges  
DROP CONSTRAINT FK_UserChallenge; 

ALTER TABLE ChallengesAccepted  
DROP CONSTRAINT FK_UserChallengeAccepted; 

ALTER TABLE ChallengesAccepted
DROP PRIMARY KEY;

ALTER TABLE ChallengesAccepted
ADD PRIMARY KEY (UserId, ChallengeId);