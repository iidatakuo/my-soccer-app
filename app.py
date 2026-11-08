import streamlit as st
from PIL import Image

# 1. Webページのタイトル設定
st.set_page_config(page_title="大会結果・速報サイト", page_icon="⚽")
st.title("⚽ 第42回 全道O-50サッカー大会 速報")

st.write("現場から送信された最新の試合結果・対戦表です。")

# 2. 画像をアップロードする機能
uploaded_file = st.file_uploader("📸 試合結果の画像（スマホの写真など）を選択してください", type=["jpg", "jpeg", "png"])

# 3. 画像が選択されたら、画面に大きく表示する
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("【最新】試合結果・対戦表")
    # アップロードされた画像を画面に表示
    st.image(image, caption="送信された結果用紙", use_container_width=True)
    st.success("最新の試合結果が表示されました！")
else:
    st.info("上の「Browse files」ボタンから、試合結果の画像を選択してください。")