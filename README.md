# Vaultify 🔐 -- Fortify Your Digital Life

## About
🔐 Vaultify is a modern, offline-first password manager designed to simplify and secure your digital life. Built with a focus on privacy and usability, Vaultify empowers users to take full control of their credentials without relying on the cloud.

From the moment you log in, the clean dashboard displays total saved passwords and provides automatic strength classification — labeling them as easy, medium, or strong using custom logic. Just provide a website URL, and Vaultify intelligently detects the platform (e.g., Google, Netflix) and organizes your entries accordingly.

All passwords are encrypted using Fernet symmetric encryption and securely stored in a local database — making sure no one but you has access. Vaultify also includes a custom password generator and supports QR code scanning (via OpenCV) and generation for seamless sharing across devices.

Going beyond just login credentials, Vaultify lets users view saved Wi-Fi passwords, manage categorized entries, and access a dynamic settings panel to fine-tune features like change fonts, font colors, GUI Style, etc..

Whether you’re a privacy enthusiast or just tired of forgetting passwords, Vaultify offers a secure, intelligent, and user-friendly solution that stands out in both functionality and design.

![Vaultify Logo](Assets/logo1.png)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Security Architecture](#security-architecture)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Dashboard Overview** — Instantly see your total passwords and their strength distribution.
- **Automatic Strength Classification** — Passwords are labeled *Easy*, *Medium*, or *Strong* with color cues.
- **Smart Platform Detection** — Provide a URL and Vaultify auto‑tags the platform (e.g., *Google*, *Netflix*).
- **Fernet‑Encrypted Database** — All data is encrypted at rest with symmetric AES‑128 (Fernet).
- **Custom Password Generator** — One‑click creation of secure passwords with length & character controls.
- **QR Code Tools** — Scan (OpenCV) or generate QR codes to move credentials between devices securely.
- **Wi‑Fi Password Vault** — View & share stored Wi‑Fi credentials via QR.
- **Dynamic Settings** — change fonts, font colors, GUI Style, etc.
- **Offline‑First** — No external servers; full privacy by design.

---

## Demo

![Screenshot 2025-07-01 071901](https://github.com/user-attachments/assets/1377de2f-8ce9-4c4b-b629-9497b46501c7)

![Screenshot 2025-07-01 071923](https://github.com/user-attachments/assets/89376e9d-5e80-4668-99b5-76f64cca0d2e)

![Screenshot 2025-07-01 071943](https://github.com/user-attachments/assets/0e1c803f-c7f5-4e2b-96ce-87ab3ecd5133)

![Screenshot 2025-07-01 071955](https://github.com/user-attachments/assets/eb667cc2-3b28-491b-91db-28521bc7a26f)

![Screenshot 2025-07-01 072008](https://github.com/user-attachments/assets/60967003-d8c8-44c5-9c22-0470b56a0499)

![Screenshot 2025-07-01 072022](https://github.com/user-attachments/assets/e24e38ff-188c-422a-b814-0803081b37bf)

![Screenshot 2025-07-01 072038](https://github.com/user-attachments/assets/05f1df63-d83b-4df3-96e5-dbeee067043b)

![Screenshot 2025-07-01 072052](https://github.com/user-attachments/assets/24c04f6f-215e-4ed6-bfee-58cd2eb670a4)

---



## Tech Stack

| Area        | Tech                                | Purpose                          |
|-------------|-------------------------------------|----------------------------------|
| **Language**| Python 3.10+                        | Core application logic           |
| **GUI**     | [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern desktop UI |
| **DB**      | SQLite                              | Lightweight local storage        |
| **Crypto**  | `cryptography` (Fernet)             | Password encryption & decryption|
| **QR**      | `opencv-python`, `qrcode`           | Scan & generate QR codes         |

---

## Getting Started

### Prerequisites
- Python >= 3.10
- `pip` package manager
- A webcam (for QR scanning) — optional but recommended

### Installation
```bash
# Clone the repo
git clone https://github.com/codex-yv/vaultify.git
cd vaultify


python setup.py

# Run Vaultify
python vaultify.py
```

> **Tip:** Use `python -OO` for a slightly smaller byte-code footprint in production.



## Security Architecture

- **Encryption** — Every record is encrypted client-side using a unique key derived from your master password (PBKDF2 + Fernet).
- **No Plaintext** — Passwords never touch disk or memory in plaintext longer than necessary.
- **Clipboard Timeout** — Auto-clears copied passwords (default 30 s).
- **Panic PIN** — A decoy PIN that instantly wipes the local vault.
- **Open Source** — Code is public for transparency and auditing.

---

## Future Roadmap
- Browser autofill extension (Chrome/Firefox)
- Mobile client (Flutter) with secure file import
- Opt-in cloud sync with end-to-end encryption
- Continuous breach monitoring via HaveIBeenPwned API

---

## Contributing

We welcome pull requests! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

> All contributions must pass the pre-commit hooks (`black`, `isort`, `flake8`).

---

## License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## Contact

Youraj Verma • [LinkedIn](https://www.linkedin.com/in/youraj-verma-929383317/) • [Email](mailto:you@example.com)

---

## Acknowledgements
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the gorgeous widgets
- [Python Cryptography](https://cryptography.io/) team for robust crypto primitives
- Hackonomics 2025 organizers for the opportunity to build Vaultify
