import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import random

st.sidebar.title("Danh sách nghệ sĩ")
selected_artist = st.sidebar.selectbox("Chọn nghệ sĩ", ["Son Tung MTP", "Deamn", "Sandaru Sathsara"])
videos = {
    "Son Tung MTP": [
        ("Top 1", "https://www.youtube.com/watch?v=FN7ALfpGxiI"),
        ("top 2", "https://www.youtube.com/watch?v=knW7-x7Y7RE"),
        ("top 3", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Special", "https://www.youtube.com/watch?v=qGRU3sRbaYw")
    ],
    "Deamn": [
        ("top 1", "https://www.youtube.com/watch?v=EFFfVjItjyo"),
        ("top 2", "https://www.youtube.com/watch?v=RfXLyP2_XbA"),
        ("top 3", "https://www.youtube.com/watch?v=8r77kgMe3-g"),
        ("spectial", "https://www.youtube.com/watch?v=nTOSd0zLZGk")
    ],
    "Sandaru Sathsara": [
        ("top 1", "https://www.youtube.com/watch?v=ecBco63zvas"),
        ("top2", "https://www.youtube.com/watch?v=SD5rXkzA5u8"),
        ("top 3", "https://www.youtube.com/watch?v=BRpIMXBa7_Q"),
        ("special", "https://www.youtube.com/watch?v=3WRKjDsG6zk")
    ]
}
st.title("Ứng dụng cuộc sống hằng ngày- sức khỏe, âm nhạc và tin tức")
tab1, tab2, tab3, tab4 = st.tabs(["Music"," Kiem tra suc khoe", "Tin tung moi nhat", "Game"])
with tab1:
    st.header(f"Bài hát của {selected_artist}")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)

with tab2:
    st.header("Kiem tra suc khoe")
    tabC, tabD, tabE, tabF =  st.tabs(["thoi gian su dung may va giac ngu", "Bmi", "luong nuoc can uong", "So luong buoc chan"])
    with tabC: 
        tabZ, tabY = st.tabs(["Dự đoán giờ đi ngủ", "Dự đoán ngủ cho trẻ sơ sinh(mới tập đi), trẻ em,người lớn"]) 
        with tabZ:
            st.title("Dự đoán giờ ngủ qua thời gian sử dụng máy")
            x = [
                [10,1,8],
                [20,5,6],
                [25,8,3],
                [30,6,5],
                [35,2,9],
                [40,4,3]
            ]
            y = [10,8,6,7,9.5,9]
            model = LinearRegression()
            model.fit(x,y)
            st.write("nhap thong tin ca nhan: ")
            age = st.number_input("tuoi cua ban", min_value= 5, max_value=100, value = 25)
            activity = st.slider("muc do hoat dong the chat cua ban(1= it, 10 = rat nhieu)",1,10,5)
            screen_time = st.number_input("thoi gian su dung man hinh cua ban trong 1 ngay(gio)", min_value=0, max_value=24, value = 6)

            if st.button("Du doan ngay"):
                input_data = [[age, activity, screen_time]]
                result = model.predict(input_data)[0]
                st.success(f" ban nen ngu khoang {result:.1f} moi dem")

                if result < 6.5:
                    st.warning("co the ban can nghi ngoi, nghi de cai thien suc khoe")
                elif result > 9:
                    st.info("ban dang vat dong nhieu, hay nghi ngoi")
                else:
                    st.success("luong ngu ly tuong")
        with tabY:
            st.title("Dự đoán ngủ cho trẻ sơ sinh(mới tập đi), trẻ em,người lớn")
            taby1, tapy = st.tabs(["Cho trẻ sơ sinh", "Cho trẻ em và người lớn"])
            with taby1:
                st.header("Tính giờ ngủ cho trẻ sơ sinh")
                thang = st.number_input("Nhập số tháng tuổi: ", min_value= 0, max_value=12, value = 1, step = 1)
                if st.button('tính thời gian ngủ theo tháng tuổi'):
                    if thang < 4:
                        st.info('cần ngủ 14-17 tiếng mỗi ngày')
                    else:
                        st.info('cần ngủ 12- 15 tiếng mỗi ngày')
            with tapy:
                st.header('Tính giờ ngủ cho trẻ em và người lớn')
                tuoi = st.number_input('Nhập độ tuổi của bạn: ', min_value=0, max_value=100, value = 18, step = 1)
                if st.button("tính thời gian ngủ"):
                    if tuoi < 3:
                        st.info("cần ngủ 11-14 tiếng mỗi ngày")
                    elif tuoi < 6:
                        st.info("cần ngủ 10-13 tiếng mỗi ngày")
                    elif tuoi < 14:
                        st.info("cần ngủ 9-11 tiếng mỗi ngày")
                    elif tuoi < 18:
                        st.info("cần ngủ 8-10 tiếng mỗi ngày")
                    elif tuoi < 65:
                        st.info("cần ngủ 7-9 tiếng mỗi ngày")
                    else:
                        st.info("cần ngủ 7-8 tiếng mỗi ngày")

    with tabD:
        weight = st.number_input("nhập cân nặng vào(kg): ", min_value= 1.0, max_value = 200.0, value = 75.0, step = 0.1)
        height = st.number_input("Nhập chiều cao(M): ", min_value= 1.0, max_value = 2.5, value = 1.7, step = 0.01)
        bmi_min =  18.5
        bmi_max = 24.9
        weight_min = bmi_min * height **2
        weight_max = bmi_max * height **2
        if st.button(" tinh bmi"):
            bmi = weight / (height ** 2)
            st.success(f"chỉ số BMI của bạn là : {bmi:.2f}")

            if bmi < 18.5:
                st.write(" Thiếu cân. Ăn thêm đi")
                tang_can = bmi - weight_min
                st.write(tang_can)
            elif 18.5 <= bmi < 24.9:
                st.info("Bình thường, Duy trì đi")
            elif 25 <= bmi < 29.9:
                st.warning(" Thừa cân, Giảm cân đi")
                giam_can = weight_max - bmi_max
                st.write(bmi_max)
            else:
                st.error("Béo phì,khám bác sĩ đi")
    with tabE:
        age = st.number_input("Nhập tuổi vào:", min_value=1, max_value= 100, value = 18, step = 1)
        if st.button ("Kiểm tra lượng nước cần uống"):
            if age < 4:
                st.info("khuyến cáo, 1.3l/ngày")
            elif 4 <= age <= 8:
                st.info("khuyến cáo, 1.7l/ngày")
            elif 9 <= age <= 13:
                st.info("khuyến cáo, 2.1l hoặc 2.4/ngày")
            elif 14 <= age <= 18:
                st.info("khuyến cáo, 2.3l hoặc 3.1l/ngày")
            elif 19 <= age <= 50:
                st.info("khuyến cáo, 2.7l/ngày với nữ, 3.7l/ngày với nam")
            elif age > 50:
                st.info("tầm 2.0 đến 3.0 lít/ngày, tùy vào mức độ hoạt động")
            else:
                st.warning("Nhập hợp lệ vào")
    with tabF:
        age3 = st.number_input("Nhap tuoi vao", min_value=1, max_value = 100, value = 18, step = 1)
        if  st.button("kiem tra so luong buoc chan nen di"):
            st.success(f"Tuoi cua ban: {age3:.0f}")
            if age3 < 18:
                st.info("Ban nen di **12,000-15,000** moi ngay")
            elif 17 < age3 <= 39:
                st.info("Ban nen di **8,000-10,000** moi ngay")
            elif 39 < age3 <=64:
                st.warning("Ban nen di **7,000-9,000** moi ngay")
            elif age3 > 64:
                st.warning("Ban nen di **6,000-8,000** moi ngay")
            else:
                st.error("Co loi xay ra, kiem tra lai thong tin")
with tab3:
    st.header("TIN TUC MOI NHAT")
    tabA, tabB, tabH = st.tabs(["TIN TUC MOI NHAT", "Gia Vang","the thao"])
    with tabA:
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

    with tabB:
        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
        gold_value = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "Giá vàng" in entry.summary.lower()]
        
        if gold_value:
            for entry in gold_value[:5]:
                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)
        else:
            st.warning("khong tim thay gia vang hien nay")
    with tabH:
        feed =  feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")
        for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

with tab4:
    st.header("Game đoán số bí mật từ 1- 100")
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.tries = 0
    guess = st.number_input("Nhập số dự đoán 1- 100", min_value = 1, max_value = 100, step = 1)
    if st.button("Đoán"):
        st.session_state.tries += 1
        if guess < st.session_state.secret:
            st.warning("số bí mật lớn hơn")
        elif guess > st.session_state.secret:
            st.warning("Số bí mật nhỏ hơn")
        else:
            st.success(f"chính xác, bán đoán đúng sau {st.session_state.tries} lần.")
    if st.button("chơi lại"):
        st.session_state.secret = random.randint(1,100)
        st.session_state.tries = 0

