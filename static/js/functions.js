def hendle_upload_file(f):
  with open('blog/static/fileupload'+f.name'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)
