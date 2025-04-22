# app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to Demo App</h1>
        <form action="/search" method="get">
            <input type="text" name="query">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return f"<h2>Search Results for: {query}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009, debug=True)
