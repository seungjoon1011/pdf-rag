### PDF 문서를 Vector DB에 저장하고 Semantic Search와 로컬 LLM을 결합한 RAG 기반 문서 질의응답 시스템

### 프로젝트 목적

기업 내부 문서, 기술 문서, 자격증 자료 등 다양한 PDF를 업로드하고 해당 문서의 내용을 기반으로 사용자의 질문에 답변할 수 있는 **문서 기반 AI 시스템**을 구축한다.

### 프로젝트 핵심

- PDF 문서 업로드 및 관리
- PDF에서 텍스트 추출
- 문서 Chunking
- Embedding 생성
- Postgresql + pgvector를 이용한 Vector 저장
- Cosine Distance 기반 유사도 검색
- 검색 결과를 LLM Context로 사용
- LM Studio + Qwen 기반 로컬 LLM
