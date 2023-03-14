CREATE TABLE settings (
    id int NOT NULL AUTO_INCREMENT,
    setting_name varchar(255) NOT NULL,
    value text(65535),
    type ENUM('text','password','bool','number','language','url') NOT NULL,
    minVal int,
    maxVal int,
    PRIMARY KEY (id)
);
CREATE TABLE wifi (
    id int NOT NULL AUTO_INCREMENT,
    ssid varchar(255) NOT NULL,
    open int DEFAULT 0,
    pwd varchar(255),
    priority int DEFAULT 1,
    hidden int DEFAULT 0,
    PRIMARY KEY (id)
);
CREATE TABLE devices (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    type ENUM(speaker,microphone,button) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO settings (setting_name,type,minVal,maxVal)
VALUES ('adm_pwd','password',NULL,NULL),
('default_wifi_ssid','text',NULL,NULL),
('default_wifi_pwd','password',NULL,NULL),
('webu_user','text',NULL,NULL),
('webu_server','url',NULL,NULL),
('webu_school','text',NULL,NULL),
('webu_pwd','password',NULL,NULL),
('webu_class','text',NULL,NULL),
('short_answer','bool',NULL,NULL),
('language','language',NULL,NULL);