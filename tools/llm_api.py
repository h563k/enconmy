import re
import json
from http import HTTPStatus, client
from openai import OpenAI
from tools.setting import ModelConfig
from tools.standard_log import log_to_file

config = ModelConfig()


def llm_gpt(prompt, system_prompt='你是一个中文助理', model_name='gpt-4') -> str:
    conn = client.HTTPSConnection("api.chatanywhere.tech")
    payload = json.dumps({
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    })
    headers = {
        'Authorization': config.llm['gpt'],
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def openai_response(prompt, system_prompt, model_types, client: OpenAI, stream=False) -> str:
    response = client.chat.completions.create(
        model=model_types,
        seed=42,
        temperature=config.llm['temperature'],
        presence_penalty=config.llm['presence_penalty'],
        frequency_penalty=config.llm['frequency_penalty'],
        max_tokens=config.llm['max_tokens'],
        stream=stream,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
    )
    if stream:
        full_response = ""
        for chunk in response:
            delta = chunk.choices[0].delta.content
            full_response += str(delta)
        return full_response
    else:
        return response.choices[0].message.content


def llm_free(prompt, system_prompt, model_types, stream=False) -> str:
    port, token = getattr(config, model_types)
    header = {
        "Content-types": "application/json",
        "Authorization": f"Bearer {token}"
    }
    client = OpenAI(base_url=f"http://192.168.28.5:{port}/v1/",
                    api_key="not used actually",
                    default_headers=header
                    )
    return openai_response(system_prompt, prompt, model_types, client, stream)


@log_to_file
def local_openai(prompt, system_prompt, model_name, stream) -> str:
    model_name = model_name if model_name else config.llm['model_name']
    if model_name in ['qwen', 'kimi', 'glm', 'spark']:
        return llm_free(prompt, system_prompt,  model_name, stream)
    elif 'gpt' in model_name:
        return llm_gpt(prompt, system_prompt, model_name)
    else:
        return '请选择合适模型'
