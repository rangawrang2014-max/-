const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

client.on('qr', (qr) => {
    qrcode.generate(qr, {small: true});
    console.log('Scan the QR code above with WhatsApp');
});

client.on('ready', () => {
    console.log('✅ البوت جاهز للعمل!');
});

client.on('message', async (msg) => {
    if (msg.body === 'قائمة' || msg.body === 'هلا') {
        msg.reply('مرحباً بك! اختر طلبك:\n1. المواد التموينية\n2. المنظفات\n3. تواصل مع الإدارة');
    }
});

client.initialize();
