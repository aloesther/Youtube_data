from .apis import youtube;
from flask import Flask;
app = Flask(__name__);


youtube._init_(app);
dataformat._init_(app);


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)