from works.citicsinfo import citicsinfo_main
from works.legu import legu_main
from tools.echobot import robot_send_message
from tools.llm_api import local_openai

if __name__ == '__main__':
    # response = local_openai(
    #     prompt="请问2024年10月13号这天，互联网对于股市的看法是悲观还是乐观？",
    #     system_prompt="你是一个金融专家",
    #     model_name='glm',
    #     stream=False
    # )
    # print(type(response))
    # robot_send_message(response)
    legu_main()