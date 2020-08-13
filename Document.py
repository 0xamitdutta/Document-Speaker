import os
import PyPDF2
import docx
from gtts import gTTS
import re
from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)

def getTextDocs(file_path):
    if(os.path.exists(file_path)):
        pass
    else:
        print("File does not exist")
        exit()

    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ('/n'.join(fullText))

def getTextTxt(file_path):
    if(os.path.exists(file_path)):
        pass
    else:
        print("File does not exist")
        exit()

    f = open(file_path, "r")
    return(f.read())

def fromTxt(file_path):
    string_words = getTextTxt(file_path)
    print(string_words)
    tts = gTTS(text=string_words, lang='en')
    tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
    os.system("start C:/Users/ranjan/Desktop/listen_pdf.mp3")

def fromDocs(file_path):
    string_words = getTextDocs(file_path)
    print(string_words)
    tts = gTTS(text=string_words, lang='en')
    tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
    os.system("start C:/Users/ranjan/Desktop/listen_pdf.mp3")

def fromPDF(file_path):
   
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
      page = pdffile.getPage(pageno)
      content = page.extractText()
      textonly = re.findall(r'[a-zA-Z0-9]+', content)
      for word in textonly:
          string_words = string_words + ' ' + word
   
  print(string_words)
  tts = gTTS(text=string_words, lang='en')
  tts.save("C:/Users/amitc/Desktop/listen_pdf.mp3")
  os.system("start C:/Users/amitc/Desktop/listen_pdf.mp3")

@app.route('/')
def upload_file():
  return '<html>
            <body>
            <form action = "http://localhost:5000/upload" method = "POST" enctype = "multipart/form-data">
                <input type = "file" name = "file">
                <input type = "submit">
            </form>
            </body>
          </html>'
  
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      ext = f.filename.split('.')
      if ext[1] == "pdf":
        fromPDF(f.filename)
      elif ext[1] == "docx":
        fromDocs(f.filename)
      elif ext[1] == "txt":
        fromTxt(f.filename)
      else:
        print('Invalid File')
      return ('file generated successfully')
    
if __name__ == '__main__':
   app.run(debug = True)
