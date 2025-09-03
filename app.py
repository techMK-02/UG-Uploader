from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SudoR2spr Repository</title>
    <link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png" />
    <style>
        body {
            background-color: #121212;
            color: #ff4c4c;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 2rem;
        }
        .container {
            display: inline-block;
            background-color: #222;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 0 15px #ff4c4caa;
        }
        a.card {
            color: #ff4c4c;
            text-decoration: none;
            font-family: monospace;
            font-size: 1.1rem;
            white-space: pre-line;
            display: block;
        }
        footer {
            margin-top: 5rem;
            padding: 1rem;
            background-color: #222;
            color: #eee;
            font-size: 0.9rem;
        }
        footer img {
            vertical-align: middle;
            margin: 0 0.5rem;
            width: 40px;
            height: 40px;
            object-fit: contain;
        }
    </style>
</head>

<body>
    <div class="container">
        <a href="https://github.com/nikhilsaini098" class="card" aria-label="GitHub link">
              />▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
              />██░▄▄▄░█░▄▄▀█▄░▄██░▀██░█▄░▄██
              />██▄▄▄▀▀█░▀▀░██░███░█░█░██░███
              />██░▀▀▀░█░██░█▀░▀██░██▄░█▀░▀██
              />▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

            <b>v2.0.0</b>
        </a>
    </div>

    <footer>
        <img loading="lazy" src="https://tinypic.host/images/2025/04/28/IMG_20250428_085026_585.jpg" alt="Logo" />
        Powered By Dev
        <img loading="lazy" src="https://tinypic.host/images/2025/04/28/IMG_20250428_085026_585.jpg" alt="Logo" />
        <div>
            <p>© 2024 Video Downloader. All rights reserved.</p>
        </div>
    </footer>
</body>

</html>
"""


if __name__ == "__main__":
    app.run()
