from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>System Monitor Dashboard</title>
            <style>
                body {
                    background-color: #0a0a0a;
                    color: #00ff99;
                    font-family: "Courier New", monospace;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                table {
                    border: 2px solid #00ff99;
                    border-collapse: collapse;
                    text-align: center;
                    min-width: 450px;
                    box-shadow: 0 0 20px #00ff99;
                }
                th, td {
                    border: 1px solid #00ff99;
                    padding: 12px 20px;
                    font-size: 16px;
                }
                h1 {
                    color: #00ff99;
                    text-align: center;
                    margin-bottom: 20px;
                    text-shadow: 0 0 10px #00ff99;
                }
                .container {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>System Monitor Dashboard</h1>
                <table>
                    <tr>
                        <th>Timestamp</th>
                        <th>CPU (%)</th>
                        <th>Memory (%)</th>
                        <th>Processes</th>
                    </tr>
                    <tr id="data-row">
                        <td colspan="4">Loading...</td>
                    </tr>
                </table>
            </div>
            <script>
                async function updateData() {
                    try {
                        const res = await fetch('/data');
                        const data = await res.json();
                        const row = document.getElementById('data-row');
                        row.innerHTML = `
                            <td>${data.timestamp}</td>
                            <td>${data.cpu_percent}</td>
                            <td>${data.memory_percent}</td>
                            <td>${data.process_count}</td>
                        `;
                    } catch (error) {
                        console.error("Error fetching data:", error);
                    }
                }
                setInterval(updateData, 1000);
                updateData();
            </script>
        </body>
    </html>
    '''

@app.route('/data')
def data():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    processes = len(psutil.pids())
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'timestamp': timestamp,
        'cpu_percent': cpu,
        'memory_percent': memory,
        'process_count': processes
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

