# Robot Cleaner Backend

FastAPI backend for the Robot Cleaner application.

## Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- PostgreSQL (if running locally without Docker)

## Setup Instructions

### 1. Create Virtual Environment

#### On macOS/Linux:
```bash
# Navigate to the BE directory
cd BE

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### On Windows:
```bash
# Navigate to the BE directory
cd BE

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

### 2. Install Dependencies

Once the virtual environment is activated, install all required packages:

```bash
pip install -r requirements.txt
```