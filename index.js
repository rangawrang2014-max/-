const { Telegraf } = require('telegraf');

// التوكين الخاص بك تم وضعه هنا بنجاح
const bot = new Telegraf('8792368712:AAH1l87zZjNcX52lLNrCCa9q-0tCBDxrJDY');

bot.start((ctx) => {
    ctx.reply('أهلاً بك يا جمعة في بوت التحميل السريع! 🚀\nأرسل لي أي رابط فيديو (تيك توك، إنستغرام، فيسبوك) وسأقوم بمعالجته.');
});

bot.on('text', async (ctx) => {
    const url = ctx.message.text;
    if (url.includes('http')) {
        ctx.reply('⏳ جاري فحص الرابط ومعالجته... يرجى الانتظار');
        // هنا سنضيف كود جلب الروابط المباشرة في الخطوة القادمة
    } else {
        ctx.reply('⚠️ يرجى إرسال رابط فيديو صحيح يبدأ بـ http');
    }
});

bot.launch();
console.log("Bot is running...");
