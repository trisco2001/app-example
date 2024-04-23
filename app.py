from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# URL of the sidecar service
SIDECAR_URL = "http://localhost:5000/get-file"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fetch-file", methods=["GET"])
def fetch_file():
    # Get the file path from the query parameter
    file_path = request.args.get("path")
    if not file_path:
        return render_template("index.html", error="File path is required")

    # Construct the full URL to call the sidecar API
    full_url = f"{SIDECAR_URL}?path={file_path}"

    try:
        # Make a GET request to the sidecar API
        response = requests.get(full_url)
        response.raise_for_status()

        # Assuming the file's contents are text-based for display in the HTML
        file_contents = response.text
        return render_template("file_info.html", file_path=file_path, file_contents=file_contents, sidecar_url=SIDECAR_URL)
    except requests.RequestException as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
