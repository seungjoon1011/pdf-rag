from openai import OpenAI


MODEL_NAME = "qwen3.5-9b-deepseek-v4-flash"

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
)

def generate_answer(
    question: str,
    context: str,
):
    prompt = f"""
다음 문서 내용을 참고해서 질문에 답변하세요.

반드시 제공된 문서 내용을 우선적으로 사용하세요.
문서에 없는 내용은 추측하지 마세요.
문서에서 답을 찾을 수 없다면
"문서에서 관련 내용을 찾을 수 없습니다."라고 답변하세요.

[문서 내용]
{context}

[질문]
{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content