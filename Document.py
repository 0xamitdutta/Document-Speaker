import os
import PyPDF2
from gtts import gTTS
import re
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)


def pdf_to_mp3(file_path):
  if(os.path.exists(file_path)):
      pass
  else:
      print("File does not exist")
      exit()
   
  f = open(file_path, 'rb')
  pdffile = PyPDF2.PdfFileReader(f)

  if(pdffile.isEncrypted):
    pdfReader.decrypt('your_password')

  no_of_pages = pdffile.getNumPages()
   
   
  string_words = ''
  for pageno in range(no_of_pages):
      pi = pdffile.getPage(pageno)
      page = pdffile.getPage(pageno)
      content = page.extractText()
      textonly = re.findall(r'[a-zA-Z0-9]+', content)
      for word in textonly:
          string_words = string_words + ' ' + word
   
  print(string_words)
  tts = gTTS(text=string_words, lang='en')
  tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
  os.system("mpg321 C:/Users/ranjan/Desktop/listen_pdf.mp3")


@app.route('/')
def upload_file():
  return '<html><body> <form action = "http://localhost:5000/upload" method = "POST" enctype = "multipart/form-data"><input type = "file" name = "file" /><input type = "submit"/></form></body></html>'
  
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      ext = f.filename.split('.')
      if ext[1] == "pdf":
        pdf_to_mp3(request.files['file'].filename)
      else:
        print('Invalid File')
      return ('file generated successfully')
    
if __name__ == '__main__':
   app.run(debug = True)
