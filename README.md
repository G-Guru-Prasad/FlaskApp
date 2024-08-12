# Flask Data Processing Application

## Overview
This Flask application simulates a simplified data retrieval and processing system. It includes endpoints for fetching data, processing it, storing it in memory, and retrieving the processed data.

## Features
- **API Endpoint for Data Retrieval (`/fetch-data`)**: Simulates fetching data from an external service.
- **Data Processing (`/process-data`)**: Processes the fetched data by transforming it.
- **In-memory Data Storage**: Stores processed data temporarily in memory.
- **API Endpoint for Retrieving Processed Data (`/get-processed-data`)**: Retrieves the processed data stored in memory.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/G-Guru-Prasad/FlaskApp
    cd FlaskApp
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the app
1. **Run the app:**
    ```bash
    python app.py
    ```
