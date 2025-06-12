# langchain_pjt
langchain project_investment report

* git clone 시 주의사항
 - git clone (link) . <- 띄어쓰고 .을 안찍으면 레포지터리 폴더(서브 폴더)가 별도로 생성됨
 - 레포지터리 폴더를 그대로 가져오고 싶으면 git clone (link)만 하면됨

* 코드 상에서 .은 상위 폴더를 의미

'''
기본 환경 셋팅
- 콘다 가상환경 만들고, 활성화 하기
conda create -n lc_env python=3.12
conda activate lc_env

- 작업디렉토리 이동
cd langchain_pjt
기본 설치 라이브러리
pip install -Uq python-dotenv
pip install -U langchain 
pip instlla -U langchain_community

- openai 
pip install -U langchain-openai 
데이터 수집 및 표현
- 주식 데이터
pip install yfinance

- 검색 엔진
pip install meilisearch

- 마크다운
pip install tabulate

- 웹 backend, frontend 개발
pip install streamlit

'''

# 앱 실행 방법
'''
streamlit run main_app.py
'''

# meilisearch 실행 방법
'''
./meilisearch --master-key="MEILISEARCH_API"
'''