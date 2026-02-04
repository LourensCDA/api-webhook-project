# API / WEBHOOK project

This project provides for two scenarios:
Scenario 1 - a simple lead API requiring users to authenticate using an API key to send leads to the API endpoint

![API Scenario 1](./Basic%20API%20-%20Send%20Lead.png)

Scenario 2 - retrieve specific lead outcomes using the lead ID and the API key.

![Lead UML](./Basic%20API%20-%20Lead%20UML.png)

Scenario 3 - a webhook endpoint that accepts lead data via POST requests and does a process. In this case, it just logs the data to a file.

## Features

- API endpoint for submitting leads with authentication via API key.
- Webhook endpoint for receiving any data with hook reference.
- Webhook hook management (create, read, update, delete).
- Lead outcome retrieval using lead ID and API key.
- Basic validation and error handling.
- Logging of lead submissions and webhook calls.
- Retrictions on lead retrieval for the original submitter only.

## Technologies Used

- Python
  - FastAPI
  - Uvicorn
  - Pydantic
  - SQLAlchemy
- PostgreSQL
- Docker (optional)
