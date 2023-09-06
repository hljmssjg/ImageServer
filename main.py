from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# 设置上传文件夹路径和下载文件夹路径
UPLOAD_FOLDER = 'upload'
DOWNLOAD_FOLDER = 'download'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return "File uploaded successfully"
    return render_template('upload.html')

@app.route('/download')
def download_page():
    files = os.listdir(app.config['DOWNLOAD_FOLDER'])
    return render_template('download.html', files=files)

@app.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(host='192.168.0.100', port=5000)
