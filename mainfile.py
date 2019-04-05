import pandas as pd
from flask import Flask
import SimpleHTTPServer
import SocketServer

app = Flask(__name__)


# Function routing the characters in the browser
@app.route('/')
def characters():
    df = pd.read_csv("characters.csv")
    return df.to_html()


# Function below shows the episodes and seasons where some characters died.
@app.route('/episodes')
def episodes():
    # print'Episodes where characters died or not.'
    ep = pd.read_csv("episode_per_season.csv")
    return ep.to_html()


# Run in Flask
# To see the episodes function, use URL 127.0.0.1/5000/episodes
if __name__ == '__main__':
    app.debug = True
    app.run()


# server_config
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 5000), Handler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    raise KeyboardInterrupt()
