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

![Screenshot 1](https://github.com/user-attachments/assets/659c9e3e-1b70-479c-96ec-77f14a28dacc)

![Screenshot 2](https://github.com/user-attachments/assets/dc602773-a085-4a6a-a701-c2aa633215a2)

![Screenshot 3](https://github.com/user-attachments/assets/2e8a84c4-ec97-461a-8d98-7891a46427cd)

![Screenshot 4](https://github.com/user-attachments/assets/695da839-e5b4-4c69-8e12-ff9b72d7f645)

![Screenshot 5](https://github.com/user-attachments/assets/ba8fc76e-ae38-4a00-b347-f516a02ce61a)

![Screenshot 6](https://github.com/user-attachments/assets/62b799e7-410f-4d22-966f-68b7d2cd94d2)

![Screenshot 7](https://github.com/user-attachments/assets/6c34a67f-e128-4916-89f5-0a24867482aa)

![Screenshot 8](https://github.com/user-attachments/assets/ce4b8a8c-4716-420a-be83-41f6cdfb7acd)

![Screenshot 9](https://github.com/user-attachments/assets/353f0303-a89a-4d4b-a98b-f5046033dc20)

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
