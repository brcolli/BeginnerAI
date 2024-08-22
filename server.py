from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue
from worker import predict_task
import hashlib
import json

# Create a Flask app
app = Flask(__name__)

# Connect to Redis on host="redis" and port=6379
redis_conn = _____
queue = Queue(connection=redis_conn)


# Create a cache key from the input data
def create_cache_key(input_data):
    data_str = json.dumps(input_data, sort_keys=True)
    return hashlib.md5(data_str.encode("utf-8")).hexdigest()


@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    input_data = data["input"]

    # Check the cache
    cache_key = create_cache_key(input_data)

    # Use the Redis connection redis_conn to attempt to get the cache_key
    cached_result = _____

    if cached_result:
        # Result is cached
        return jsonify({"prediction": int(cached_result)})

    # Result is not cached

    # Enqueue the task if not in cache
    job = queue.enqueue(predict_task, input_data)

    # Use the Redis connection redis_conn to store the result in the cache once it's done
    def store_result(job, connection, result, *args, **kwargs):
        _____

    job.on_success = store_result

    return jsonify({"job_id": job.get_id()})


@app.route("/result/<job_id>", methods=["GET"])
def get_result(job_id):

    # Fetch the job from the queue using the job_id to see the status
    job = _____
    if job.is_finished:
        return jsonify({"prediction": job.result})
    else:
        return jsonify({"status": job.get_status()}), 202


if __name__ == "__main__":
    app.run(debug=True)
