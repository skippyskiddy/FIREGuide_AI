## FIRE Financial Advisor App

A financial advisor application built with FastAPI on the backend, React on the frontend, integrated with OpenAI's GPT-4 for a chatbot feature, and SQLite for the database.

### Prerequisites

- Python 3.7+
- Yarn (for the frontend)

### Setup & Installation

1. **Backend Setup**:

    a. Clone the repository:

    ```bash
    git clone <your-repo-link>
    cd <your-repo-directory-name>
    ```

    b. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

    c. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    d. Set up the SQLite database:

    ```bash
    python
    >>> from database.base import Base
    >>> from database.database import engine
    >>> Base.metadata.create_all(bind=engine)
    ```

    e. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. **Frontend Setup**:


### Usage

1. Open your web browser and navigate to `http://localhost:3000` to access the frontend.

2. Interact with the chatbot and input your budgeting details to get financial advice aligned with FIRE principles.

3. Check the statistics column on the right for a breakdown of your financial details and advice from the chatbot.
