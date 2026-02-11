# Real-Time Threat Detection Platform

## Overview

An async, event-driven distributed system for ingesting logs,
detecting threats in real time, and generating alerts.

## Architecture Flow

Client
  ↓
Log Ingestion Service (FastAPI)
  ↓
Kafka Topic: raw-logs
  ↓
Threat Analysis Service
  ↓
Kafka Topic: threat-events
  ↓
Alert Service
  ↓
PostgreSQL

## Tech Stack

- FastAPI (Async)
- aiokafka
- Redis (Sliding Window Detection)
- PostgreSQL
- Docker
- GitHub Actions (CI/CD)
