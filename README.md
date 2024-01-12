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

## Testing the API Endpoints

To test the API endpoints, you can use the interactive documentation provided by FastAPI. Open a web browser and navigate to either of the following URLs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

In the documentation, you will find a list of API endpoints, including /translate and /translate/jeringoza. Follow these steps to test the endpoints:

Enter text and choose options in the UI to test the /translate and /translate/jeringoza endpoints.
Click the "Execute" button to send a request to your FastAPI backend.