# SentinelShield: Advanced Intrusion Detection & Web Protection System

## Overview
SentinelShield is a lightweight Intrusion Detection and Web Protection System that simulates the behavior of a Web Application Firewall. It inspects HTTP requests, detects malicious payloads, applies rate limiting, logs events, and displays alerts on a dashboard.

## Features
HTTP request inspection  
Signature-based attack detection  
Rate limiting for brute-force prevention  
SQLite logging system  
Real-time dashboard visualization  

## Technologies Used
Python  
Flask  
SQLite  
Regex Pattern Matching  
HTML  

## Attack Detection
The system detects common web attacks such as:
SQL Injection  
Cross Site Scripting  
Local File Inclusion  
Command Injection  

## How It Works
Incoming requests are analyzed by the detection engine. If malicious patterns are identified, the request is blocked, logged in the database, and displayed on the dashboard.

## Usage
Run the application:
python app.py

Open browser:
http://127.0.0.1:5000/


<img width="1920" height="1080" alt="Screenshot (687)" src="https://github.com/user-attachments/assets/1f7f7e54-ed7b-4d0a-9c2f-e25dde21eec6" />


Test attacks:
http://127.0.0.1:5000/test?input=1' OR '1'='1

<img width="1920" height="1080" alt="Screenshot (689)" src="https://github.com/user-attachments/assets/da911824-85af-41d0-a981-82a0a3617353" />



View dashboard:
http://127.0.0.1:5000/dashboard


<img width="1920" height="1080" alt="Screenshot (691)" src="https://github.com/user-attachments/assets/c884b5b0-6476-4c0f-9e4b-d4321b2fc0ad" />


## Outcome
This project demonstrates a working mini WAF and IDS system suitable for cybersecurity practical learning and portfolio demonstration.
