from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>YouTube Downloader</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">

<div class="bg-white p-6 rounded-xl shadow-xl w-full max-w-md">
  <h2 class="text-2xl font-bold mb-4 text-center">YouTube Downloader</h2>

  <form method="post">
    <input name="video_url" required placeholder="YouTube URL"
      class="w-full border p-2 rounded mb-3">

    <input name="save_path" value="downloads"
      class="w-full border p-2 rounded mb-3">

    <button class="bg-blue-500 text-white w-full p-2 rounded">
      Fetch Formats
    </button>
  </form>

  {% if formats %}
  <form action="/download" method="post" class="mt-4">
    <input type="hidden" name="video_url" value="{{ video_url }}">
    <input type="hidden" name="save_path" value="{{ save_path }}">

    {% for f in formats %}
      <label class="block mb-2">
        <input type="radio" name="format_id" value="{{ f['format_id'] }}" required>
        {{ f['ext'] }} - {{ f.get('height', 'NA') }}p
      </label>
    {% endfor %}

    <button class="bg-green-500 text-white w-full p-2 rounded mt-3">
      Download
    </button>
  </form>
  {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["video_url"]
        save_path = request.form["save_path"]

        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = [
                f for f in info["formats"]
                if f.get("vcodec") != "none" and f.get("acodec") != "none"
            ]

        return render_template_string(
            HTML,
            formats=formats,
            video_url=url,
            save_path=save_path
        )

    return render_template_string(HTML)


@app.route("/download", methods=["POST"])
def download():
    url = request.form["video_url"]
    save_path = request.form["save_path"]
    format_id = request.form["format_id"]

    os.makedirs(save_path, exist_ok=True)

    ydl_opts = {
        "format": format_id,
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)

    return send_file(
        file_path,
        as_attachment=True,
        download_name=os.path.basename(file_path)
    )


if __name__ == "__main__":
    app.run(debug=True)
