# Duo Admin API Custom Reporting Tool

This Python script leverages the Duo Admin API to generate custom reports on administrator actions. It allows filtering by action type and application name, providing enhanced reporting capabilities beyond the standard Duo Admin Panel.

## Prerequisites

- Python 3.6 or higher
- Duo Admin API credentials (Integration Key, Secret Key, and API Hostname)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/gdikeako/duo_reports.git
   cd duo-admin-reporting
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root directory with your Duo Admin API credentials:
   ```
   DUO_IKEY=your_integration_key
   DUO_SKEY=your_secret_key
   DUO_HOST=your_api_hostname
   ```

## Usage

Run the script:
```
python filter_admin_logs.py
```

Follow the prompts to filter logs by action and application name.
