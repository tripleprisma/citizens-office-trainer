from flask import Flask
import urllib.request

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello World!'


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


if __name__ == '__main__':
  app.run()