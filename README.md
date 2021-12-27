# calculator
python3 app/tests/api_response.py -v

docker build -t calculator-api .
docker run --name calculator-api-container -d -p 5000:5000 calculator-api 