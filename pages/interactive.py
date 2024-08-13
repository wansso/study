import streamlit as st
st.title("상호작용을 위한 앱 만들기")
st.write("https://www.naver.com/")
st.link_button("네이버 바로가기", "https://www.naver.com/")
st.image("https://www.google.com/imgres?q=.gif&imgurl=https%3A%2F%2Fmir-s3-cdn-cf.behance.net%2Fproject_modules%2Fmax_1200%2F5eeea355389655.59822ff824b72.gif&imgrefurl=https%3A%2F%2Fwww.behance.net%2Fgallery%2F55389655%2Fgif-Collection-Two%3Flocale%3Dko_KR&docid=uubrj_0qSRPkUM&tbnid=o6_r7euBpEAGgM&vet=12ahUKEwjKuMmT3vGHAxUTe_UHHeTeCfkQM3oECGUQAA..i&w=800&h=600&hcb=2&ved=2ahUKEwjKuMmT3vGHAxUTe_UHHeTeCfkQM3oECGUQAA")
col1, col2 = st.columns(2)
with col1:
    st.image("https://www.google.com/imgres?q=.gif&imgurl=https%3A%2F%2Fmir-s3-cdn-cf.behance.net%2Fproject_modules%2Fmax_1200%2F5eeea355389655.59822ff824b72.gif&imgrefurl=https%3A%2F%2Fwww.behance.net%2Fgallery%2F55389655%2Fgif-Collection-Two%3Flocale%3Dko_KR&docid=uubrj_0qSRPkUM&tbnid=o6_r7euBpEAGgM&vet=12ahUKEwjKuMmT3vGHAxUTe_UHHeTeCfkQM3oECGUQAA..i&w=800&h=600&hcb=2&ved=2ahUKEwjKuMmT3vGHAxUTe_UHHeTeCfkQM3oECGUQAA")
with col2:
    st.success("이미지예요!")
    st.info("이 캐릭커 이름은 무엇일까요?")
    answer = st.text_input("이 캐릭터의 이름을 써 주세요.")
    if answer =="쪼랩"
        st.success("맞았습니다!")
    else :
        st.warning("다시 생각해 보세요.")

tab1, tab2 = st.tabs(["봄", "여름"])
tab1.success("봄이예요")
tab2.info("여름이예요")