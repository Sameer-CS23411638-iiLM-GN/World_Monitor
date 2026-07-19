# World Monitor

A simple Python Flask app for tracking world status by location.

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate it:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows Command Prompt:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Usage

Open `http://127.0.0.1:5000` in your browser.

## Files

- `app.py` - Flask web server
- `templates/index.html` - UI page
- `static/css/styles.css` - Basic styling
- `requirements.txt` - Python dependencies
