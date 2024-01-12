# LanguageWire Translation API

This project implements a simple REST API using FastAPI to perform translations and Jeringoza translations.

## Project Structure

- `main.py`: The FastAPI application.
- `translation`: Contains translation-related modules.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: Dependencies required for the project.

## Setup

### Prerequisites

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [Googletrans](https://pypi.org/project/googletrans==4.0.0-rc1/)

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd language_translation

2. **Create a Virtual Environment:**

- python -m venv venv
- source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'

3. **Install Dependencies:**

- pip install -r requirements.txt

4. **Run the Application:**

- uvicorn main:app --reload
