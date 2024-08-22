# BeginnerAI
App for beginner AI learning

Look in generate_model.py, worker.py, and server.py for incomplete lines:
_____
And fill them in, following the hints.

Start by installing the requirements:
pip install -r requirements.txt

Then with generate_model.py. Run it using:
python generate_model.py

Once this successfully completes, proceed to fixing worker.py and server.py.

When you are ready, start the Docker container using:
docker-compose up --build

Then in another terminal you can run:
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"input": [5.1, 3.5, 1.4, 0.2]}'

This should output a scaled transformed vector on the input.