# File Signature Change

**Educational tool for exploring file signature (magic bytes) manipulation and format identification mechanisms.**

---

## 🚧 DISCLAIMER

> **This tool is intended strictly for educational and research purposes.**
>
> Unauthorized use of this tool to bypass file type checks, deceive systems, or perform malicious actions is **strictly prohibited**. The author is not responsible for any damage, misuse, or legal consequences arising from its use.

---

## 📌 Overview

**SigChange** is a lightweight utility that allows users to modify the **magic bytes** (file signatures) of a file in order to:

- Study how systems and applications determine file types.
- Understand vulnerabilities in magic byte-based detection mechanisms.
- Experiment with file inspection and reverse engineering tools.

This is useful for students, security researchers, and digital forensics enthusiasts who wish to understand file format validation at the byte level.

---

## 🔍 What Are Magic Bytes?

Magic bytes are the first few bytes at the beginning of a file that indicate its format (e.g., `0xFF 0xD8` for JPEG, `0x89 0x50` for PNG). Many systems use these values to determine file types rather than relying solely on file extensions.

---

## 🛠 Features

- Replace magic bytes with a user-defined or preset signature.
- Support for common file types (JPEG, PNG, PDF, ZIP, etc.).
- CLI-based interface for ease of automation.
- Cross-platform compatible (Tested on Windows and Linux).

---

## 🚀 Usage

### Prerequisites

- Python 3.x

### Example

```bash
python sigChange.py example.asp png
