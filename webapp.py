from flask import Response, render_template
from markupsafe import escape

from algorithm import gen_frames
from project import app, socket


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed/<path:source>")
def video_feed(source=0):
    if source == "0":
        source = 0
    source = escape(source)
    return Response(
        gen_frames(source),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":
    app.run(debug=True)
