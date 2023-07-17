import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt

# Khởi tạo ứng dụng Firebase
cred = credentials.Certificate('bigdata-eec24-firebase-adminsdk-n4a82-94ef80532e.json')  # Thay đổi đường dẫn đến tệp serviceAccountKey.json
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_data():
    data = {}
    collection_ref = db.collection('top_20_ratio')
    docs = collection_ref.stream()
    for doc in docs:
        category = doc.get('name')
        pledged = float(doc.get('pledged_goal_ratio'))
        data[category] = pledged

    return data

def plot_chart(data):
    categories = list(data.keys())
    pledged_values = list(data.values())


    fig, ax = plt.subplots()
    ax.bar(categories, pledged_values)
    ax.set_xlabel('Name')
    ax.set_ylabel('Pledged ratio')
    ax.set_title('Top 20 Ratio')
    fig.set_size_inches(10, 6)  # Điều chỉnh kích thước biểu đồ theo ý muốn
    plt.xticks(rotation=90)

    fig.subplots_adjust(bottom=0.2, top=0.9)

    st.pyplot(fig)


# Streamlit interface
st.title('Top 20 Ratio')

data = get_data()
plot_chart(data)
