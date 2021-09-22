from flask import Flask, render_template, request, send_file
from pytube import YouTube

app= Flask(__name__)

yt= None

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/view", methods=["POST", "GET"])
def view():
  global yt
  video= {}
  try:
      print("\nAccessing the URL...\n")
      yt= YouTube(request.form["url"])
  except:
    return "Connection Error"

  video["img"]= yt.thumbnail_url
  video["title"]= yt.title
  video["desc"]= yt.description
  st= []
  for s in yt.streams.filter(progressive=True):
    q= {}
    q["itag"]= s.itag
    q["res"]= s.resolution
    q["mime_type"]= s.mime_type
    q["size"]= round((s.filesize/1000000),2)
    st.append(q)
  for s in yt.streams.filter(type="audio"):
    q= {}
    q["itag"]= s.itag
    q["res"]= s.abr
    q["mime_type"]= s.mime_type
    q["size"]= round((s.filesize/1000000),2)
    st.append(q)
  video["streams"]= st

  return render_template("download.html", video=video)

@app.route("/download/<tag>")
def download(tag):
  global yt
  strm= yt.streams.get_by_itag(int(tag))
  strm.download()
  print("Downloaded!")
  return send_file(strm.default_filename, as_attachment=True)

if __name__ == "__main__":
  app.run()