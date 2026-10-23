from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Vaccine Repository</title>
    <style>
        :root {
            --bg: #0f172a;
            --panel: #111827;
            --card: #1f2937;
            --primary: #4f46e5;
            --accent: #22c55e;
            --text: #e5e7eb;
            --muted: #9ca3af;
            --border: #334155;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #0f172a, #111827 35%, #1e293b);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 24px;
        }

        .container {
            width: min(920px, 100%);
            background: rgba(17, 24, 39, 0.9);
            border: 1px solid var(--border);
            border-radius: 20px;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
            overflow: hidden;
        }

        .header {
            padding: 32px 32px 18px;
            border-bottom: 1px solid var(--border);
            background: rgba(79, 70, 229, 0.08);
        }

        .badge {
            display: inline-block;
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 12px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            background: rgba(34, 197, 94, 0.15);
            color: var(--accent);
            border: 1px solid rgba(34, 197, 94, 0.4);
            margin-bottom: 16px;
        }

        h1 {
            margin: 0 0 8px;
            font-size: clamp(2rem, 4vw, 3.2rem);
            line-height: 1.1;
        }

        .subtitle {
            margin: 0;
            color: var(--muted);
            font-size: 1.04rem;
        }

        .content {
            padding: 32px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 10px;
        }

        .card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 22px;
        }

        .label {
            font-size: 0.8rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 10px;
        }

        .value {
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0;
        }

        .language-bar {
            height: 14px;
            background: #0b1220;
            border: 1px solid var(--border);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 20px;
        }

        .language-fill {
            height: 100%;
            width: 68%;
            background: linear-gradient(90deg, var(--primary), #8b5cf6);
            border-radius: inherit;
        }

        .notes {
            margin-top: 26px;
            line-height: 1.7;
            color: var(--text);
        }

        ul {
            margin: 10px 0 0 18px;
            padding: 0;
            color: var(--muted);
        }
    </style>
</head>
<body>
    <main class=\"container\">
        <header class=\"header\">
            <div class=\"badge\">Python Web Page</div>
            <h1>Vaccine Repository</h1>
            <p class=\"subtitle\">Repository: jovitaprabu/vaccine</p>
        </header>

        <section class=\"content\">
            <div class=\"grid\">
                <div class=\"card\">
                    <div class=\"label\">Repository ID</div>
                    <p class=\"value\">1430693995</p>
                </div>

                <div class=\"card\">
                    <div class=\"label\">Language Focus</div>
                    <p class=\"value\">Python</p>
                </div>

                <div class=\"card\">
                    <div class=\"label\">Status</div>
                    <p class=\"value\">Ready</p>
                </div>
            </div>

            <div class=\"card\" style=\"margin-top:20px;\">
                <div class=\"label\">Language Composition</div>
                <p class=\"value\" style=\"font-size:1.2rem;\">Python-based project content</p>
                <div class=\"language-bar\" aria-label=\"Python language usage\">
                    <div class=\"language-fill\"></div>
                </div>
            </div>

            <div class=\"notes\">
                <p>This simple webpage is created using Python only, without external libraries, and follows the course syllabus limit for a lightweight, browser-ready page.</p>
                <ul>
                    <li>Server: Python standard library</li>
                    <li>Page: HTML generated directly in Python</li>
                    <li>Run locally with: python app.py</li>
                </ul>
            </div>
        </section>
    </main>
</body>
</html>
"""


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(PAGE.encode("utf-8"))

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()
