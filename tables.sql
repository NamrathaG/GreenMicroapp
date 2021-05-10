CREATE TABLE Users (
    EmailId varchar(255) NOT NULL,
    UserName varchar(255) NOT NULL,
    PRIMARY KEY (EmailId)
);

CREATE TABLE Challenges (
    Id int NOT NULL IDENTITY(1, 1),
    Title varchar(255) NOT NULL,
    Description varchar(255) NULL,
    CreatorId varchar(255),
    CreatedDate date NOT NULL,
    EndDate date NULL,
    Active BIT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (CreatorId) REFERENCES Users(EmailId)
);

ALTER TABLE Challenges
ADD ImageUrl varchar(512);


CREATE TABLE ChallengesAccepted (
    Id int NOT NULL IDENTITY(1, 1),
    UserId varchar(255) NOT NULL,
    ChallengeId int NOT NULL,
    Completed BIT NOT NULL,
    PhotoUrl varchar(MAX),
    Comment varchar(255),
    Reward int NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (UserId) REFERENCES Users(EmailId),
    FOREIGN KEY (ChallengeId) REFERENCES Challenges(Id)
);