'''
testing:
接口地址：https://vip-hk-s1.zeabur.app
APIkey：sk-TDF6zgxVQqAfYNYuE2Eb3334F13d4d9780594dAa6eF364C5

my_paid = "sk-G4C6rzryzKe7fzUN2c65553694454dD9915eC1DeDb0fA128"

gpt-4-1106-preview

dall-e-3

'''

from openai import OpenAI

def chat_gpt_openai(content):
    api_key = 'sk-G4C6rzryzKe7fzUN2c65553694454dD9915eC1DeDb0fA128'
    api_base = 'https://vip-hk-s1.zeabur.app/v1'

    client = OpenAI(api_key=api_key, base_url=api_base)

    rsp = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages=[
            {"role": "user", "content": content}
        ],
            temperature=0,
            stream=True,
            timeout=600
        )
    text = ''
    for chunk in rsp:
        if chunk.choices[0].finish_reason is None and chunk.choices[0].delta.content is not None:
            text += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")

        # if chunk.choices:
        #     for choice in chunk.choices:
        #         print(choice.delta.content)
    return text

content = 'Ok'
print(chat_gpt_openai(content))














'''
按量计费费用 = 分组倍率 × 模型倍率 × （提示token数 + 补全token数 × 补全倍率）/ 500000 （单位：美元）
The fee based on usage = Group Rate × Model Rate × (Prompt token count + Completion token count × Completion Rate) / 500,000 (unit: US dollars).

group_rate = 1
model_rate = {
    "gpt-3.5-turbo": 0.75,
    "gpt-3.5-turbo-0301": 0.75,
    "gpt-3.5-turbo-0613": 0.75,
    "gpt-3.5-turbo-1106": 0.5,
    "gpt-3.5-turbo-16k": 1.5,
    "gpt-3.5-turbo-16k-0613": 1.5,
    "gpt-3.5-turbo-instruct": 0.75,
    "gpt-4": 15,
    "gpt-4-0314": 15,
    "gpt-4-0613": 15,
    "gpt-4-1106-preview": 5,
    "gpt-4-32k": 30,
    "gpt-4-32k-0314": 30,
    "gpt-4-32k-0613": 30,
    "gpt-4-vision-preview": 5
}


completion_rate = {
    "gpt-3.5-turbo": 3,
    "gpt-3.5-turbo-0125": 3,
    "gpt-3.5-turbo-0301": 3,
    "gpt-3.5-turbo-0613": 3,
    "gpt-3.5-turbo-1106": 3,
    "gpt-3.5-turbo-16k": 1.33,
    "gpt-3.5-turbo-16k-0613": 1.3333,
    "gpt-3.5-turbo-instruct": 1.3333,
    "gpt-3.5-turbo-instruct-0914": 1.3333,
    "gpt-4": 2,
    "gpt-4-0125-preview": 3,
    "gpt-4-0314": 2,
    "gpt-4-0613": 2,
    "gpt-4-1106-preview": 3,
    "gpt-4-32k": 2,
    "gpt-4-32k-0314": 2,
    "gpt-4-32k-0613": 2,
    "gpt-4-turbo-preview": 3,
    "gpt-4-vision-preview": 3,
}




'''