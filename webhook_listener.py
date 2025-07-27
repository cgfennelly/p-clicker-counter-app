from flask import Flask, request
import subprocess
import threading

app = Flask(__name__)

def run_deploy():
    # Call the deploy script
    subprocess.call(["./deploy.sh"])

@app.route('/payload', methods=['POST'])
def payload():
    # Optionally, add verification logic here
    # Launch deployment in a separate thread so the response is fast
    threading.Thread(target=run_deploy).start()
    return "Deployment triggered", 200

if __name__ == '__main__':
    # Listen on all interfaces, port 5000
    app.run(host='0.0.0.0', port=8076)
