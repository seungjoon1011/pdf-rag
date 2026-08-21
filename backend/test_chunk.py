from app.services.chunk_service import split_text


text = """
SQL은 관계형 데이터베이스를 관리하기 위한 언어이다.
SELECT는 데이터를 조회할 때 사용한다.
WHERE는 특정 조건에 맞는 데이터를 필터링한다.
GROUP BY는 데이터를 특정 기준으로 그룹화한다.
HAVING은 그룹화된 결과에 조건을 적용한다.
ORDER BY는 조회 결과를 정렬한다.
"""


chunks = split_text(
    text,
    chunk_size=100,
    overlap=20,
)


for index, chunk in enumerate(chunks):
    print("=" * 50)
    print(f"CHUNK {index}")
    print("=" * 50)
    print(chunk)