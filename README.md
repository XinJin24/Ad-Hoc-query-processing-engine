# CS562 Team Project: Ad-Hoc Query Processing Engine
Team Members

    Su Zhang
    Xin Jin

Technology Stack

    Python: Main programming language.
    PostgreSQL: Database system used for storing and querying data.
    Psycopg2: Python-PostgreSQL Database Adapter for connecting and operating on the database.
    pytest: Testing framework to run Python tests.
    python-dotenv: Library for loading environment variables from .env files into os.environ.
    tabulate: Utility for formatting output tables in a human-readable form.

Setup Instructions
1. Clone the Repository

Clone the project repository to your local machine using the following commands:

bash

git clone https://github.com/XinJin96/Ad-Hoc-query-processing-engine.git
cd Ad-Hoc-query-processing-engine

2. Environment Setup

Set up and activate a Python virtual environment:

bash

python -m venv venv
# On Unix/macOS
source venv/bin/activate  
# On Windows
venv\Scripts\activate

3. Install Dependencies

Install the required dependencies by running:

bash

pip install -r requirements.txt

Ensure you have a requirements.txt file in your project directory with these contents:

makefile

attrs==22.2.0
iniconfig==2.0.0
packaging==23.0
pluggy==1.0.0
psycopg2==2.9.5
pytest==7.2.2
python-dotenv==1.0.0
tabulate==0.9.0

4. Configure Environment Variables

Create a .env file at the root of your project directory and specify your PostgreSQL credentials:

makefile

USER=YOUR_USERNAME
PASSWORD=YOUR_PASSWORD
DBNAME=YOUR_DB_NAME

Adjust the USER, PASSWORD, and DBNAME placeholders to match your PostgreSQL setup.
5. Database Setup

Ensure your PostgreSQL database is correctly configured and accessible with the credentials specified in the .env file.
6. Running the Project

Run the project's main script from the project directory:

bash

python generated.py