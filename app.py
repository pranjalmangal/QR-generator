from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    content_type = request.form['content_type']
    content = request.form['content']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/qrcode.png')

    return render_template('result.html', content_type=content_type)

@app.route('/download_qr')
def download_qr():
    return send_file('static/qrcode.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
