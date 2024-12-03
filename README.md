# TelegramQuickReplyBot
Telegram中支持按钮的自定义消息发送机器人。作为快速回复很方便。Telegram supports custom message-sending bots with buttons, making quick replies very convenient.

[English Readme](https://github.com/MiHaKun/TelegramQuickReplyBot/blob/master/README.en.md)

# 简介
TG八卦水群的时候，总是希望有个快捷回复。同时，受限于Telegram的政策，想回复按钮消息基本是不可能的，是的，你是高级会员也没这功能。

所以，就开发了一个简单的InlineBot，可以方便的回复消息，顺便添加几个url按钮。美观大方。

效果如图：
![image](https://github.com/user-attachments/assets/f6bfeec2-40fd-437e-8f2b-198b47a652e8)


激发方式：
![image](https://github.com/user-attachments/assets/0ef91fcc-3f21-4f08-80b5-fbe76eb34429)


大概的格式就是 @这个机器人 ， 空格，然后打入命令。命令可以自己配置（图例上，我使用show）

# 准备工作
1. 找 @Botfather 申请一个机器人
2. 获取机器人token
3. 打开机器人的inline mode
4. 配置 .env 文件（可以把 .env_example 改名获得）
5. 按需配置。如果需要id，可以找 @GetTheirIDBot 获取。（没错，也是我写的）

# 部署
```bash
git clone https://github.com/MiHaKun/TelegramQuickReplyBot.git
cd TelegramQuickReplyBot
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# 执行
```bash
python -m QuickReplyBot
```

# 快速回复短语配置
参看文件内的 `quick_reply.json` 。
![image](https://github.com/user-attachments/assets/ef5d0c5b-4e75-4b82-92c5-c26a655c3cb4)


效果可以看看本文档第一张图。


# ToDoList
- [ ] 增加图片和视频消息
- [ ] 做个可以托管的，省的大家自己部署了。
- [ ] 添加防止滥用的方案


# 关于

- 本产品基于Apache协议开源。
- 作者 米哈( [@MrMiHa](https://t.me/MrMiHa) )是一个苦逼程序员，不是煤场奴工，有问题别太理直气壮的跑来下命令。
- 讨论群组是 : https://t.me/DeveloperTeamGroup 欢迎加入后玩耍
- 随意Fork，记得保留`关于`的内容。
- 初版写了2小时。喜欢请打赏。不会部署，群里找我。
- 服务器推荐RackNerd的。实际上，我也确实用这个。够便宜。这款就够：[2核3G--年27刀](https://my.racknerd.com/aff.php?aff=11705&pid=828) 
- 实在搞不定部署，可以群里找大家帮忙部署下。服务器也可以找大家共用： https://t.me/DeveloperTeamGroup 
- 实在实在实在搞不定部署，找  [@MrMiHa](https://t.me/MrMiHa)  同学付费部署……
