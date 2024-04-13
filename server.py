from flask import Flask
from flask import render_template
from flask import Response, request
from markupsafe import escape

# to protect from injection attacks
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

