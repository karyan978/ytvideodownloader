✅ YouTube Downloader (Flask + yt-dlp)
🔧 COMPLETE INSTALLATION & SETUP GUIDE (Windows)
1️⃣ Python install (sabse pehle)
🔹 Check karo (agar pehle se hai)
python --version


Agar version aa jaaye → OK
Agar nahi → install karo 👇

🔹 Download link
```
👉 https://www.python.org/downloads/

```

✔ Python 3.10+
✔ Install ke time “Add Python to PATH” ✔️ tick karna

2️⃣ Project folder me jao

Example:

cd C:\Users\liger\OneDrive\Desktop\python\ytvideodownloader

3️⃣ Virtual Environment (RECOMMENDED)
🔹 Create venv
```
python -m venv venv
```
🔹 Activate venv
venv\Scripts\activate


Terminal me (venv) dikhna chahiye ✅

4️⃣ Flask install (Web App ke liye)
🔹 Command
```
pip install flask
```
🔹 Flask ka kaam

Web page banata hai

Form handle karta hai

Browser ko file download karwata hai

5️⃣ yt-dlp install (YouTube download engine)
🔹 Command
```
pip install yt-dlp
```
🔹 yt-dlp ka kaam

YouTube video info nikalna

Formats (360p / 720p / 1080p)

Video download karna

6️⃣ FFmpeg install (BEST QUALITY ke liye) 🔥

⚠️ Ye Python package nahi hai
⚠️ Ye system tool hai

🔹 Kaam kya karta hai?

Best video + best audio merge

MP4 / MP3 conversion

Quality improve

🔹 Download link
```
👉 https://www.gyan.dev/ffmpeg/builds/
```
✔ Download: ffmpeg-git-full.7z

🔹 Extract karo

Example:

C:\ffmpeg\bin\ffmpeg.exe

🔹 PATH me add karo (VERY IMPORTANT)

Start → Environment Variables

System Variables → Path

Edit → New

Paste:

C:\ffmpeg\bin


OK → OK

Terminal restart

🔹 Test
ffmpeg -version


Agar version aa gaya → DONE ✅

7️⃣ Node.js install (YouTube JS warning fix)

YouTube ab JS runtime maangta hai.

🔹 Download link
```
👉 https://nodejs.org/
```
✔ LTS version install karo
✔ Next → Next → Finish

🔹 Test
node -v


Version aaye → DONE ✅

8️⃣ Final requirements summary
🔹 Python packages
pip install flask yt-dlp

🔹 System tools

FFmpeg

Node.js

9️⃣ App run command 🚀
python downloader.py


Browser me open karo:

http://127.0.0.1:5000
