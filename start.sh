#!/bin/bash
cd /yahoo
pipenv run uvicorn run_service:app --host 0.0.0.0 --port 8000