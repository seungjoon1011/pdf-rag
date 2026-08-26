from app.services.llm_service import generate_answer


answer = generate_answer(
    question="SELECT란 무엇인가?",
    context="""
SELECT는 SQL에서 데이터를 조회하기 위해 사용하는 명령어이다.
테이블에서 원하는 데이터를 조회할 수 있다.
""",
)

print(answer)