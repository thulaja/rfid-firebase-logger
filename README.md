# RFID Firebase Logger

An RFID-based access system using **Raspberry Pi** and **Firebase Realtime Database** to log scans and control access in real-time.

---

## 🔧 Features

- Uses MFRC522 RFID reader with Raspberry Pi
- Checks RFID UID and name
- Grants or denies access with GPIO output
- Logs each scan to **Firebase** with:
  - RFID ID
  - Team name
  - Access status
  - Timestamp

---

## 🛠️ Hardware Used

- Raspberry Pi (any model with GPIO)
- MFRC522 RFID reader
- RFID tags/cards
- GPIO-connected LED or relay (pin 40)

---

## 💻 Software & Libraries

- Python 3
- `firebase-admin`
- `RPi.GPIO`
- `mfrc522`

---

## 📸 Project Images

| RFID Circuit | Firebase DB Output |
|--------------|--------------------|
| ![Circuit](photos/circuit.jpg) | ![Firebase](photos/rfid_fb.jpg) |

---

## 📜 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rfid-firebase-logger.git
cd rfid-firebase-logger
