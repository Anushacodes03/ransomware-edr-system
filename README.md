🛡️ Ransomware Detection & Response System (EDR)

A simulation-based Endpoint Detection and Response (EDR) system designed to detect ransomware activity using behavioral analysis and entropy-based encryption detection, and visualize incidents through a SOC-style web dashboard.

This project demonstrates how modern EDR solutions detect, analyze, and respond to ransomware threats at the endpoint level.

🚨 Problem Statement

Ransomware attacks can encrypt thousands of files within seconds, causing severe data loss and operational downtime.

Traditional signature-based antivirus systems often fail to detect new or unknown ransomware variants.

This project addresses the problem by implementing behavior-based detection, which identifies malicious activity based on how ransomware behaves rather than how it looks.

🎯 Objectives

Monitor file system activity in real time

Detect abnormal file modification behavior

Identify encrypted files using entropy analysis

Log ransomware incidents for forensic analysis

Provide centralized alert visualization

Simulate automated incident response

⚙️ System Architecture
File System Activity
        ↓
Behavioral Detection Engine
        ↓
Entropy-Based Encryption Analysis
        ↓
Incident Logging
        ↓
Flask REST API
        ↓
SOC Dashboard (Frontend)

🔍 Key Features
✅ Real-Time File Monitoring

Uses OS-level file system event monitoring

Detects rapid file modification patterns

✅ Behavioral Ransomware Detection

Identifies suspicious activity based on modification frequency

Prevents reliance on static malware signatures

✅ Entropy-Based Encryption Detection

Uses Shannon entropy to detect encrypted data

Differentiates normal files from ransomware-encrypted files

✅ Incident Logging

Automatically records attack details

Stores timestamp, file path, and entropy value

✅ REST API Backend

Flask-based API exposes incident data

Enables centralized monitoring

✅ SOC-Style Dashboard

Web-based alert visualization

Displays detected ransomware incidents

✅ Automated Response Simulation

Identifies suspicious running processes

Simulates process termination

Records response actions in logs

🧪 Technologies Used

Python

Watchdog (file monitoring)

Flask (backend API)

psutil (process inspection)

HTML, CSS, JavaScript

REST APIs

▶️ How to Run the Project

1️⃣ Start Backend API
cd backend
python app.py

2️⃣ Start Detection Engine
cd backend
python monitor/file_monitor.py

3️⃣ Open Dashboard

Open frontend/index.html using Live Server.

📸 Project Screenshots

Screenshots demonstrating detection, alerts, and dashboard visualization are provided below.

(Add screenshots here)

⚠️ Disclaimer

This project is developed strictly for educational and research purposes.

It is a simulation-based EDR system and does not perform kernel-level enforcement or real malware execution.

👩‍💻 Author

Anusha Upadhyay
Cybersecurity Enthusiast | Blue Team | SOC Analyst Aspirant

⭐ If you found this project useful, feel free to star the repository.
