CREATE DATABASE SFP_Mercury;

USE SFP_Mercury;

CREATE table Networks (
	ESSID char varying(30) NOT NULL,
    BSSID char varying(30) NOT NULL,
    SSID char varying(50),
    Display_Name char varying(20) default NULL,
    Type char varying(30) NOT NULL,
    AuthType char varying(20) NOT NULL,
    CryptType char varying(10) NOT NULL,

    PRIMARY KEY(ESSID, BSSID),
);

CREATE table Hosts (
	# integer primary key AUTO INCREMENT NOT NULL,
    Display_Name char varying(20) default NULL,
    MAC varchar(17) NOT NULL,
    IPv4 char(15) default "000.000.000.000",
    NetMask char(3) default "/??",
    FKCountry char(2) REFERENCES Countries(ID) ON DELETE set NULL ON UPDATE cascade,
    FKRegion char varying(30) REFERENCES Regions(Name) ON DELETE set NULL ON UPDATE cascade,
    FKTimezone char varying(30) REFERENCES Timezones(Name) ON DELETE set NULL ON UPDATE cascade,
    Latitude decimal(10,8) default 0,
    Longitude decimal(11,8) default 0,

    CHECK (MAC LIKE '^([0-9A-F]{2}-){5}[0-9A-F]{2}$')
);

CREATE table Countries (
    ID char(2) primary key NOT NULL,
    Country char varying(30),
    Continent char varying(5) default "?",
    Currency char(3) default "???"
);

CREATE table Regions (
    Name char varying(30) NOT NULL,
    FKCountry char(2) REFERENCES Countries(ID) ON DELETE cascade ON UPDATE cascade,
    
    PRIMARY KEY(RegionName, FKCountry)
);

CREATE table Timezones (
    Name char varying(30) primary key NOT NULL
);

CREATE table HostInNet (
	FKNetworks integer REFERENCES Networks(ID) ON DELETE cascade ON UPDATE cascade,
    FKHosts integer REFERENCES Hosts(ID) ON DELETE set NULL ON UPDATE cascade
);
