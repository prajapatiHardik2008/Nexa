from flask import Flask, render_template_string

app = Flask(__name__)


# Simple Dashboard HTML Structure (Tailwind included)
dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; }
        .card { background: #111; border: 1px solid #333; }
    </style>
</head>
<body class="p-8">
    <h1 class="text-3xl font-bold mb-6 text-center">NEXA V2 COMMAND CENTER</h1>
    
    <div class="grid grid-cols-2 gap-6">
        <!-- Logs Panel -->
        <div class="card p-4 h-96 overflow-y-auto">
            <h2 class="text-xl mb-2">System Logs</h2>
            <pre>{{ logs }}</pre>
        </div>
        
        <!-- Info Panel -->
        <div class="card p-4">
            <h2 class="text-xl mb-2">Current Status</h2>
            <p>Mode: <span class="text-blue-400">{{ mode }}</span></p>
            <p>Last Command: <span class="text-yellow-400">{{ last_cmd }}</span></p>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
  try:
    with open("brain/logs.txt", "r") as f:
      data = f.read()
  except FileNotFoundError:
    data = "No logs found yet."

  # <pre> tag use karne se file ki exact formatting maintain rahegi
  html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nexa Logs</title>
        <style>
            body { background-color: #0f172a; color: #38bdf8; font-family: monospace; padding: 20px; }
            h2 { color: #f43f5e; }
            pre { background-color: #1e293b; padding: 15px; border-radius: 8px; border: 1px solid #334155; }
        </style>
    </head>
    <body>
        <h2>Nexa Activity Logs</h2>
        <pre>{{ data }}</pre>
    </body>
    </html>
    """
  return render_template_string(html_template, data=data)


@app.route('/desk')
def desk():
  return render_template_string(dashboard_html,mode='normal',last_cmd="Hello NEXA")
if __name__ == "__main__":
  app.run(debug=True, port=2424, host="0.0.0.0")