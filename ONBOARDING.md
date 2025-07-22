# 🚀 Setup Guide

Welcome! This guide will help you set up and run the Rewards Redemption Optimizer project, even if you have no coding experience. Follow these steps for **Windows** or **Mac**.

---

## 1. Install Required Tools

### A. Visual Studio Code (VS Code)
- Download: https://code.visualstudio.com/
- Install for your operating system (Windows or Mac).

### B. GitHub Desktop
- Download: https://desktop.github.com/
- Install for your operating system.

### C. Python 3
- **Windows:**
  - Download: https://www.python.org/downloads/windows/
  - During installation, **check the box that says “Add Python to PATH.”**
- **Mac:**
  - Download: https://www.python.org/downloads/macos/
  - Or use Homebrew: `brew install python`
  - (Most Macs already have Python 3, but it’s good to update.)

---

## 2. Clone the Project Repository

1. Open GitHub Desktop.
2. Click “File” → “Clone repository.”
3. Paste the project’s GitHub URL (ask your teammate for the link if needed).
4. Choose a folder to save the project and click “Clone.”

---

## 3. Open the Project in VS Code

1. In GitHub Desktop, click “Open in Visual Studio Code” (or open VS Code and use “File” → “Open Folder”).
2. Select the project folder you just cloned.

---

## 4. Set Up Python Virtual Environment

### A. Open a Terminal in VS Code
- In VS Code, go to “Terminal” → “New Terminal.”

### B. Create a Virtual Environment
- **Windows:**
  ```sh
  python -m venv venv
  ```
- **Mac:**
  ```sh
  python3 -m venv venv
  ```

### C. Activate the Virtual Environment
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac:**
  ```sh
  source venv/bin/activate
  ```

You should see `(venv)` at the start of your terminal prompt.

---

## 5. Install Project Dependencies

With the virtual environment activated, run:
```sh
pip install -r requirements.txt
```

---

## 6. Run the Backend (API Server)

In the terminal (with venv activated), run:
```sh
uvicorn backend.main:app --reload
```
- The backend will start at `http://localhost:8000`.

---

## 7. Run the Frontend (Streamlit App)

Open a **new terminal** (and activate the venv again if needed):

- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac:**
  ```sh
  source venv/bin/activate
  ```

Then run:
```sh
streamlit run frontend/app.py
```
- The frontend will start at `http://localhost:8501`.

---

## 8. Using the App

- Open your browser and go to `http://localhost:8501`.
- Enter your search details and see the results!

---

## 9. Tips

- If you close VS Code or the terminal, you’ll need to activate the venv again before running commands.
- If you get errors about missing packages, make sure you’re in the venv and run `pip install -r requirements.txt` again.

---

## 10. Extra: GitHub Desktop for Updates

- To get the latest code, open GitHub Desktop and click “Fetch origin” or “Pull origin.”

---

If you get stuck at any step, copy the error message and ask your teammate for help! 