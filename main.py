from tools.stocks import get_stock_data
from tools.echobot import robot_send_message
from tools.llm_api import local_openai

if __name__ == '__main__':
    response = local_openai(
        prompt="你好,你喜欢我吗",
        system_prompt="你是一个中文助理",
        model_name='qwen',
        stream=False
    )
    print(response)
    