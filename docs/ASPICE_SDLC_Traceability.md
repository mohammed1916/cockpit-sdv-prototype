# ASPICE/SDLC Traceability Documentation

## Requirements Traceability Matrix (RTM)

| **Requirement**              | **Design**                                       | **Implementation**                                | **Testing**                                | **Verification**                                |
| ---------------------------- | ------------------------------------------------ | ------------------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Telemetry Data Handling      | Azure Function collects and forwards data        | `send_telemetry` Azure Function                   | Unit test for data processing              | Verified via Azure logs and Android integration |
| Cockpit Display (UI)         | Designed using Jetpack Compose                   | `MainActivity.kt` fetches and displays data       | Manual UI testing with live/mock data      | Verified with simulated data from API           |
| Infotainment ECU Simulation  | Flask REST API returns dynamic telemetry         | `infotainment-service/app.py` in Docker container | Docker container test + API curl           | Validated through Android integration           |
| CI/CD Automation             | GitHub Actions Pipeline                          | `.github/workflows/ci-cd-pipeline.yml`            | Auto-tests + container run + curl API test | Verified via CI/CD logs and actions             |
| End-to-end Cloud Integration | Data flows: Docker → Azure Function → Android UI | All components connected                          | Full-stack test using mock/demo flow       | Confirmed using mock + real Azure call tests    |

---

## SDLC Phases Mapped to Prototype

### 1. **Requirements**

- Real-time vehicle telemetry display (speed, battery, location/media)
- Connectivity between simulated ECU, cloud, and cockpit
- Adherence to ASPICE traceability and CI/CD

### 2. **Design**

- Modular system: domain controller (Docker) + backend (Azure) + UI (Android)
- Interfaces: REST APIs, HTTP calls, cloud triggers
- Mock-compatible and CI/CD friendly

### 3. **Implementation**

- Dockerized Flask app as simulated ECU
- Azure Function for cloud ingestion
- Jetpack Compose UI for cockpit display

### 4. **Testing**

- Component testing: Docker API, Azure function logic
- System testing: Integration flow via GitHub pipeline
- UI testing: Visual + telemetry rendering on Android

### 5. **Deployment**

- GitHub Actions for CI/CD and Azure deployment
- Docker image run locally or remotely
- Android app fetches telemetry every 2s

### 6. **Maintenance**

- Cloud logs for failure analysis
- Easy update of Docker/Function code via pipeline
- Mock API fallback for demo resilience

### 7. **Verification & Validation**

- Verified flow with both mock and real Azure backend
- Validation through logs, UI feedback, and API monitoring
