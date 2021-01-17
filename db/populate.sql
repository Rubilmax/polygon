CREATE TABLE Trackings (
    tracking_id INT NOT NULL AUTO_INCREMENT,
    status_code INT NOT NULL,
    completion_time FLOAT NOT NULL,
    request_datetime DATETIME NOT NULL,
    PRIMARY KEY ( tracking_id )
);
