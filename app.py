from flask import Flask, request, render_template, jsonify
import requests
import datetime
from swagger_client.api.storage_api import StorageApi
from swagger_client.api.utilities_api import UtilitiesApi
from swagger_client.models.models_file_data import ModelsFileData
from swagger_client.models.models_health_check_response import ModelsHealthCheckResponse

app = Flask(__name__)

SIDECAR_URL = "http://localhost:8080/api/v1/storage/download-file"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health-check")
def healthCheck():
    utilities_api = UtilitiesApi()

    start = datetime.datetime.now()
    try:
        health_check_result: ModelsHealthCheckResponse = utilities_api.health_check()
        healthy = health_check_result.healthy
        end = datetime.datetime.now()
    except Exception as ex:
        healthy = str(ex)
        end = datetime.datetime.now()

    execution_time_ms = round(((end - start).total_seconds() * 1000), 4)

    return render_template(
        "index.html", 
        health_check_result=healthy, 
        execution_time_ms=execution_time_ms,
    )


@app.route("/fetch-file", methods=["GET"])
def fetch_file():
    # Get the file path from the query parameter
    file_path = request.args.get("path")
    if not file_path:
        return render_template("index.html", error="File path is required")

    storage_api = StorageApi()
    try:
        models_file_data = storage_api.download_file(file_path)

        # Assuming the file's contents are text-based for display in the HTML
        file_contents = models_file_data.content
        return render_template("file_info.html", file_path=file_path, file_contents=file_contents, sidecar_url=SIDECAR_URL)
    except requests.RequestException as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
