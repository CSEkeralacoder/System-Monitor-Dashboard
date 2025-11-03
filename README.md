# Real-Time Intrusion Detection and GUI Monitor

## 🧠 Overview
This project combines a real-time intrusion detection system with a Python-based GUI monitor. It continuously tracks system activity (processes, ports, network usage, etc.) and uses AI/anomaly detection to flag suspicious behavior. The GUI interface allows easy monitoring of security events, system status, and logs. Developed as part of a cybersecurity project integrating detection, visualization, and response.

## ⚙️ Features
- Real-time process monitoring
- Network port scanning and visualization
- Lightweight GUI built using Tkinter
- Detection script integrated with GUI interface
- Custom logging for security events
- Compatible with Python 3.9.6 and later

## 🗂️ Project Structure
project_root/
│
├── detector.py          # Main intrusion detection script
├── gui_monitor.py       # GUI interface for monitoring
├── requirements.txt     # Required Python dependencies
└── README.md            # Documentation file

## 🧩 Installation
### 1️⃣ Clone the repository
git clone https://github.com/your-username/RealTime-Intrusion-Monitor.git
cd RealTime-Intrusion-Monitor

### 2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

If you don’t have a requirements.txt file yet, create one using:
pip freeze > requirements.txt

## ▶️ Usage
### Run the Detector
python detector.py

### Run the GUI Monitor
python gui_monitor.py

The GUI window will launch and display real-time monitoring logs from the detector.

## 📊 Example Output
-------------------------------------------------
System Monitor - Real-Time Intrusion Detection
-------------------------------------------------
[INFO] Process scan running...
[ALERT] Suspicious activity detected on port 8080
-------------------------------------------------

## 🛠️ Technologies Used
- Python 3.9.6
- Tkinter – GUI framework
- psutil – Process and system utilities
- socket – Network module
- time & threading – For concurrent scanning and updates

## 🧾 Requirements
Make sure the following Python modules are installed:
psutil
tkinter
socket
threading

You can install them with:
pip install psutil

## 🧑‍💻 Developer
Vishnu P U  
Cybersecurity Enthusiast | Computer Science Engineer  
B.Tech in Computer Science, Ahalia School of Engineering and Technology  
Kerala Technological University (KTU)

## 🏁 Future Enhancements
- Add facial and fingerprint authentication integration  
- Implement live alert notifications  
- Add database for log storage (SQLite or MongoDB)  
- Integrate AI-based anomaly prediction models  

## 🪪 License
This project is licensed under the MIT License — you’re free to use, modify, and distribute it with attribution.

## 📧 Contact
For queries or collaboration:  
**Email:** vishnupu.k3@gmail.com  
**GitHub:** https://github.com/CSEkeralacoder

