from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return "Missing ?url= parameter", 400
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        return Response(
            r.content,
            status=r.status_code,
            content_type=r.headers.get("Content-Type", "application/xml"),
            headers={"Access-Control-Allow-Origin": "*"},
        )
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8086)
