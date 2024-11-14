import asyncio
from telegram import Bot
from tools.setting import ModelConfig
from tools.standard_log import log_to_file

#  消息收发机器人
@log_to_file
async def send_message(text):
    config = ModelConfig()
    telegram = config.telegram
    token = telegram['token']
    chat_id = telegram['chat_id']
    bot = Bot(token=token)
    # 使用await来等待异步操作完成
    result = await bot.send_message(chat_id=chat_id, text=text)
    # 可以进一步处理result，例如记录日志或检查发送状态
    return f"Message sent: {result}"


def robot_send_message(text):
    asyncio.run(send_message(text))
