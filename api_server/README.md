# API Server

This repository contains the backend API server for the application. The frontend code is located in the `ui-server` repository.

## Getting Started

Follow these instructions to set up and run the API server locally.

### Prerequisites

* Python 3.8+
* pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/api-server.git
    cd api-server
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The application uses `config.ini` for configuration. Ensure this file is properly set up with your database credentials and other necessary settings.

### Running the Application

To start the API server, run the `main.py` file using `uvicorn` (or similar ASGI server, if specified in `requirements.txt`):

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

This will start the server on `http://localhost:8000`. The `--reload` flag enables auto-reloading on code changes, which is useful for development.

## Project Structure

*   `api/`: Contains API endpoint definitions.
*   `app/`: Core application logic and main entry point.
*   `schemas/`: Pydantic models for request and response data.
*   `storage/`: Database connection and repository logic.
*   `helper/`: Utility functions and exception handlers.
*   `utils/`: General utility functions.
*   `config.ini`: Configuration file.
*   `requirements.txt`: Python dependencies.
