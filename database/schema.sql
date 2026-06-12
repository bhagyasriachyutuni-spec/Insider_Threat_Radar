    CREATE DATABASE threat_detection;
USE threat_detection;

CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY,
    email VARCHAR(100),
    password VARCHAR(255),
    role ENUM('admin','user'),
    security_question VARCHAR(255),
    security_answer VARCHAR(255),
    status ENUM('active','archived') DEFAULT 'active'
);

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    input_data TEXT,
    prediction VARCHAR(50),
    risk_score FLOAT,
    risk_level VARCHAR(20),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    message TEXT,
    status VARCHAR(20),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);