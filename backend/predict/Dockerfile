FROM pycaret/full

WORKDIR /code

COPY api.py .

COPY requirements.txt .

COPY model.pkl .

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7500"]