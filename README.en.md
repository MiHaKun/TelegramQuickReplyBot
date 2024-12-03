# TelegramQuickReplyBot
A Telegram bot that supports custom message sending with buttons, making quick replies very convenient.

## Introduction
When chatting in a gossip group on Telegram, it’s always nice to have a quick reply option. However, due to Telegram’s policies, replying with button messages is basically impossible, even if you are a premium member.

Therefore, I developed a simple InlineBot that allows for convenient message replies, along with a few URL buttons. It’s visually appealing.

### Example Effect:
![image](https://github.com/user-attachments/assets/f6bfeec2-40fd-437e-8f2b-198b47a652e8)

### Activation Method:
![image](https://github.com/user-attachments/assets/0ef91fcc-3f21-4f08-80b5-fbe76eb34429)

The general format is to type @this_bot, followed by a space, and then enter the command. The commands can be configured (in the example, I used "show").

## Prerequisites
1. Find @Botfather to create a bot.
2. Obtain the bot token.
3. Enable inline mode for the bot.
4. Configure the `.env` file (you can rename `.env_example` to get it).
5. Configure as needed. If you need IDs, you can find @GetTheirIDBot (yes, I also wrote this).

## Deployment
```bash
git clone https://github.com/MiHaKun/TelegramQuickReplyBot.git
cd TelegramQuickReplyBot
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Execution
```bash
python -m QuickReplyBot
```

## Quick Reply Phrase Configuration
Refer to the `quick_reply.json` file.
![image](https://github.com/user-attachments/assets/ef5d0c5b-4e75-4b82-92c5-c26a655c3cb4)

You can see the effect in the first image of this document.

## To-Do List
- [ ] Add image and video message support.
- [ ] Create a hosted version to save users from having to deploy it themselves.
- [ ] Implement measures to prevent abuse.

## About

- This product is open-sourced under the Apache license.
- The author, Mi Ha ([@MrMiHa](https://t.me/MrMiHa)), is a struggling programmer, not a coal yard slave. Please don’t come demanding commands too assertively.
- Discussion group: https://t.me/DeveloperTeamGroup. Feel free to join and have fun.
- Feel free to fork, but please retain the "About" section.
- The first version was completed in 2 hours. If you like it, consider donating. If you have trouble deploying, feel free to ask me in the group.
- Recommended server: RackNerd. In fact, I use it myself. It’s affordable. This option is sufficient: [2 cores, 3GB - $27/year](https://my.racknerd.com/aff.php?aff=11705&pid=828). 
- If you really can’t manage the deployment, you can ask people in the group for help. You can also find shared servers here: https://t.me/DeveloperTeamGroup.
- If you absolutely cannot handle the deployment, contact [@MrMiHa](https://t.me/MrMiHa) for paid deployment assistance.
