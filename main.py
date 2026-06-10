import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV 데이터 분석", layout="wide")

st.title("CSV 데이터 분석 앱")

# 파일 읽기 (파일 이름 그대로 사용)
df = pd.read_csv("ta_20260601093156.csv")

st.subheader("데이터 미리보기")
st.dataframe(df)

st.subheader("기본 정보")
st.write(f"행 개수: {df.shape[0]}")
st.write(f"열 개수: {df.shape[1]}")

st.subheader("기술 통계")
st.dataframe(df.describe())

# 숫자형 열 찾기
numeric_columns = df.select_dtypes(include="number").columns.tolist()

if len(numeric_columns) > 0:
    st.subheader("그래프")

    selected_column = st.selectbox(
        "그래프로 볼 열 선택",
        numeric_columns
    )

    st.line_chart(df[selected_column])

    st.write("막대 그래프")
    st.bar_chart(df[selected_column])

else:
    st.warning("숫자형 데이터가 없습니다.")
