from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

from string import Template

query = "안녕하세요. 오늘 날짜로 뉴욕행 비행기를 예약할 수 있나요?"

system_prompt = """
너는 항공편 관련 상담을 해주는 인공지능 에이전트야.
항공편 관련 상담에는 다음과 같은 사용자의 요청이 있을 수 있어.

항공편 예약: 사용자가 특정 날짜와 시간에 항공편을 예약하려고 할 때 해당 요청을 처리합니다.
항공편 변경 또는 취소: 이미 예약된 항공편을 변경하거나 취소하고자 할 때 이에 대한 요청을 처리합니다.
좌석 선택: 특정 좌석을 선택하거나 선호하는 좌석을 예약할 수 있도록 도와주는 요청을 처리합니다.
가격 및 할인 문의: 항공편의 가격 및 할인 정보를 문의하고 해당 정보를 제공하는 요청을 처리합니다.
수하물 정보: 수하물의 허용량, 추가 비용, 수하물 체크인 절차 등에 대한 정보를 제공하는 요청을 처리합니다.
항공편 상태 확인: 특정 항공편의 운항 상태, 지연 여부, 취소 여부 등에 대한 정보를 문의하고 해당 정보를 제공하는 요청을 처리합니다.
탑승 시 요구되는 문서: 여권, 비자 등 탑승 시 필요한 문서에 대한 정보를 문의하고 해당 정보를 제공하는 요청을 처리합니다.
환불 및 보상 요청: 항공편 취소 시 환불 절차, 보상 요청 등에 대한 요청을 처리합니다.
장애물 도움: 장애인 또는 특별한 요구사항이 있는 승객을 위한 보조 서비스 요청을 처리합니다.
기타 문의: 항공편 관련 기타 문의 사항에 대한 답변을 제공합니다.
"""

prompt_template = Template("""
다음 사용자의 요청에서 사용자의 의도를 분류해줘
질문: "$query"
사용자 의도:
""")

print(system_prompt)
print(prompt_template.substitute(query=query))

def consult(query):
  prompt = prompt_template.substitute(query=query)
  chat_completion = client.chat.completions.create(
      messages=[
          {
            "role": "system",
            "content": system_prompt,
          },
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="ggml-model-q4_k_m", #모델명 변경
  )
  return chat_completion.choices[0].message.content

def consult_seconds(query):
  prompt = prompt_template.substitute(query=query)
  chat_completion = client.chat.completions.create(
      messages=[
          {
            "role": "system",
            "content": system_prompt,
          },
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="ggml-model-q4_k_m", #모델명 변경
  )
  return chat_completion.choices[0].message.content

print(consult("안녕하세요. 항공편이 연착이되어서 문의드립니다."))