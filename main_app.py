# streamlit run main_app.py
import streamlit as st
from report_service import investment_report
# from search_index import SearchResult, search_compay
from stock_info import Stock

st.title("AI 투자 보고서 생성 서비스")
# /search_query = st.text_input("회사명", "Apple Inc")
search_query = st.text_input("회사명", "AAPL")
company_list = ["AAPL: Apple Inc",
                "APLE: Apple Hospitality REIT Inc"]

company_selected = st.selectbox("회사 선택", company_list, index=0)

tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 차트로 시각화
with tab1:
    st.header(f"{company_selected}의 6개월 주식 거래량")
    # symbol = company_selected.split(":")[0] # symbol 추출
    # stock = Stock(symbol)
    stock = Stock(search_query)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)

# LLM이 만든 투자 보고서 출력
with tab2:
    st.header(f"{company_selected} AI 투자보고서 생성")
    
    # AI 투자 보고서 출력
    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중"):
            symbol, name = company_selected.split(": ")
            report = investment_report(name, symbol)
            #report = investment_report(company_selected.name, company_selected.symbol)
            st.success("투자 보고서 생성 완료")
        st.write(report)
