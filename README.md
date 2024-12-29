# Discord Bot Login Automation

This project is a Python script that uses the **Helium** library to automate logging into Discord.

---

## 🎯 Features
- Automatically opens a browser.
- Fills in the email and password on the Discord login page.
- Presses **ENTER** to log in.

---

## 🛠️ System Requirements
Before running this code, ensure you have the following installed:
1. **Python** version 3.7 or newer.
2. **Google Chrome** as your primary browser.
3. **ChromeDriver** that matches your Chrome version. [Download here](https://chromedriver.chromium.org/downloads).

---

## 📂 Installation and Setup
1. **Clone or Download the Project**:
   - Clone this project using Git:
     ```bash
     git clone https://github.com/rizqirehan/login_automation.git
     ```
   - Or download the ZIP file and extract it.

2. **Open the Project**:
   - Open the project folder in your terminal or favorite text editor.

3. **Install Dependencies**:
   - Run the following command to install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure Login Credentials**:
   - Open the `login.py` file (or your main script file).
   - Replace the `email` and `password` values with your Discord credentials:
     ```python
     email = "your_email@example.com"
     password = "your_password"
     ```

---

## 🚀 Running the Program
1. Ensure all requirements are met.
2. Run the script using the following command in your terminal:
   ```bash
   python login.py
