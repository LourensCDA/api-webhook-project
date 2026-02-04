# API / WEBHOOK project

This project provides for two scenarios:
Scenario 1 - a simple lead API requiring users to authenticate using an API key to send leads to the API endpoint

![API Scenario 1](./Basic%20API%20-%20Send%20Lead.png)

Scenario 2 - retrieve specific lead outcomes using the lead ID and the API key.

![API Scenario 2](./Basic%20API%20-%20Get%20Lead.png)

Basic UML diagram of the Lead API structure:
![Lead UML](./Basic%20API%20-%20Lead%20UML.png)

Scenario 3 - a webhook endpoint that accepts lead data via POST requests and does a process. In this case, it just logs the data to a file.
![API Scenario 3](./Webhook.png)

Basic UML diagram of the Webhook structure:

![Lead UML](./Webhook%20UML.png)

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

## Steps to complete project

1. Design the basic processes and UML diagrams.
2. Set up Docker postgreSQL instance.
3. Set up packages
4. Create database models and migrations.
5. Implement API endpoints for lead submission and retrieval.
6. Implement webhook endpoint and hook management.
7. Add authentication and validation.
8. Test the endpoints using tools like Postman or curl.
9. Add testing and documentation.
10. Review and optimize the code.
