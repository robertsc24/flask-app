from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
        <head>
            <title>Flask App</title>
            <style>
                body {
                    background-color: #f0f0f2;
                    margin: 0;
                    padding: 0;
                    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
                    
                }
                .container {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    text-align: center;
                }
                h1 {
                    color: #333;
                    background-color: #fff;
                    display: inline-block;
                    padding: 15px 25px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello MSOE!!</h1>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)

