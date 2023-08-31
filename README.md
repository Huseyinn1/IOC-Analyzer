## IoC Enrichment Project
This project is an application that enriches the IoC (Indicator of Compromise) values given by the API by analyzing them in different sources. IoC values are data such as IP addresses, URLs, domains that are used to identify potential threats in network security. This project provides a detailed report by checking whether the IoC values are associated with malicious activities, their geographic location, whether they are blacklisted, their whois information and more.

## Technologies 
- This project is written in Python 3.11 programming language.
- FastAPI framework is used as the web API.
- PostgreSQL is used as the database. SQLAlchemy is used as the ORM.
- Poetry is used for dependency management.
- The application is containerized with Docker Compose.
- Python’s logging module is used for logging.
## Installation
To run the project, you need to have Docker and Docker Compose installed. You also need to have Poetry installed.

After cloning the project, go to the project directory and run the following command:

 - poetry install

This command will install the dependencies of the project.

Then, run the following command:

  - docker-compose up -d
 
-This command will start the PostgreSQL database and the FastAPI application.

## Usage
-The application runs at http://localhost:8001. You can access the documentation of the application at http://localhost:8001/docs.

-The application provides a /search endpoint. You can send a GET request to this endpoint with the IoC type and value to get the analysis result.
For example:


- curl http://localhost:8000/search?type=ip&value=8.8.8.8
-This request will return the analysis result of the 8.8.8.8 IP address in JSON format.

-The application currently supports three IoC types: ip, url and domain.

The application uses the following sources for analysis:

- AlienVault
- VirusTotal
- GreyNoise
- GoogleSafe
- Hetrixtools
- WhoisXmL

The application stores the analysis results in the PostgreSQL database. You can access the database by running the following command:

-docker-compose exec db psql -U postgres

This command will open the PostgreSQL command line interface. You can see the tables in the database by using the \dt command.
## Contribution
-We welcome all kinds of contributions and suggestions. Please fork this repository and make your contributions. Then create a Pull Request to share the changes.
