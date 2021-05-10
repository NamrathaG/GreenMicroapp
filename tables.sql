CREATE TABLE Users (
    EmailId varchar(255) NOT NULL,
    UserName varchar(255) NOT NULL,
    PRIMARY KEY (EmailId)
);

CREATE TABLE Challenges (
    Id int NOT NULL IDENTITY(1, 1),
    Title varchar(255) NOT NULL,
    Description varchar(255) NULL,
    ImageUrl varchar(512) NULL,
    CreatorId varchar(255),
    CreatedDate date NOT NULL,
    EndDate date NULL,
    Active BIT NOT NULL,
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
    Reward int NULL,
    PRIMARY KEY (Id),
    CONSTRAINT FK_UserChallengeAccepted FOREIGN KEY (UserId) REFERENCES Users(EmailId),
    CONSTRAINT FK_ChallengeChallengeAccepted FOREIGN KEY (ChallengeId) REFERENCES Challenges(Id) ON DELETE CASCADE
);