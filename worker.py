from rq import Queue
from rq.worker import Worker
from redis import Redis
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")

# Connect to Redis
redis_conn = Redis(host="redis", port=6379)
queue = Queue(connection=redis_conn)


# Define the task function
def predict_task(input_data):
    input_data = np.array(input_data).reshape(1, -1)
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    return int(prediction[0])


# Start a worker to process tasks
if __name__ == "__main__":
    worker = Worker([queue], connection=redis_conn)
    worker.work()
