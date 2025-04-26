# cockpit-sdv-prototype
 
# Connected Cockpit Software Prototype (Android + Azure + Docker)

This repository presents a prototype for a domain controller-based cockpit software system designed for software-defined vehicles.

## Overview

This project integrates key components of modern automotive software:

- **Android Cockpit UI**: Developed using Jetpack Compose, displaying real-time telemetry.
- **Domain Controller Simulation**: Dockerized infotainment ECU using Flask.
- **Cloud Integration**: Azure Functions simulate telemetry ingestion and processing.
- **CI/CD Pipeline**: GitHub Actions used for continuous integration and deployment.
- **ASPICE & SDLC Traceability**: Documented lifecycle phases and requirements mapping.


## Features

- Fetches real-time vehicle telemetry (speed, battery, media, etc.)
- Displays data via a responsive Android UI
- Simulated domain controller running in Docker
- Backend processing via Azure Function
- Automated deployment through GitHub Actions

## Technologies Used

- Kotlin (Jetpack Compose)
- Python (Flask)
- Docker
- Azure Functions
- GitHub Actions
- Markdown / ASPICE documentation

## Getting Started

1. Clone the repository
2. Run the Docker simulation:
   ```bash
   cd docker-domain-controller/infotainment-service
   docker build -t infotainment-service .
   docker run -p 5000:5000 infotainment-service
   ```
3. Deploy the Azure Function using the GitHub Actions pipeline
4. Launch the Android app and view telemetry

