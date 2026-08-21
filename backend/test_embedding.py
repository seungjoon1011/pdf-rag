from app.services.embedding_service import create_embedding

text = "FROM은 데이터를 조회하기 위해 사용하는 SQL 명령어이다."

embedding = create_embedding(text)

print("차원:" , len(embedding))
print("앞부분: ",embedding[:10])