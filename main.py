import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt

# Khởi tạo ứng dụng Firebase
cred = credentials.Certificate(
    'bigdata-eec24-firebase-adminsdk-n4a82-94ef80532e.json')  # Thay đổi đường dẫn đến tệp serviceAccountKey.json
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()



def get_data_top_20_category():
    data = {}
    collection_ref = db.collection('top_20_category')
    docs = collection_ref.stream()
    for doc in docs:
        category = doc.get('category')
        pledged = float(doc.get('pledged'))
        data[category] = pledged

    return data


def plot_chart_top_20_category(data):
    categories = list(data.keys())
    pledged_values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(categories, pledged_values)
    ax.set_xlabel('Category')
    ax.set_ylabel('Pledged')
    ax.set_title('Pledged Amount by Category')
    fig.set_size_inches(10, 6)  # Điều chỉnh kích thước biểu đồ theo ý muốn
    plt.xticks(rotation=90)

    fig.subplots_adjust(bottom=0.2, top=0.9)

    st.pyplot(fig)


def get_data_top_20_country():
    data = {}
    collection_ref = db.collection('top_20_country')
    docs = collection_ref.stream()
    for doc in docs:
        category = doc.get('country')
        pledged = float(doc.get('count'))
        data[category] = pledged

    return data


def plot_chart_top_20_country(data):
    categories = list(data.keys())
    pledged_values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(categories, pledged_values)
    ax.set_xlabel('Country')
    ax.set_ylabel('Count')
    ax.set_title('Top 20 Country')
    fig.set_size_inches(10, 6)  # Điều chỉnh kích thước biểu đồ theo ý muốn
    plt.xticks(rotation=90)

    fig.subplots_adjust(bottom=0.2, top=0.9)

    st.pyplot(fig)

def get_data_top_20_ratio():
    data = {}
    collection_ref = db.collection('top_20_ratio')
    docs = collection_ref.stream()
    for doc in docs:
        category = doc.get('name')
        pledged = float(doc.get('pledged_goal_ratio'))
        data[category] = pledged

    return data


def plot_chart_top_20_ratio(data):
    categories = list(data.keys())
    pledged_values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(categories, pledged_values)
    ax.set_xlabel('Name')
    ax.set_ylabel('Pledged Ratio')
    ax.set_title('Top 20 Ratio')
    fig.set_size_inches(10, 6)  # Điều chỉnh kích thước biểu đồ theo ý muốn
    plt.xticks(rotation=90)

    fig.subplots_adjust(bottom=0.2, top=0.9)

    st.pyplot(fig)


# Streamlit interface
st.title('Data Analysis App')

# Create a sidebar navigation menu
page = st.sidebar.selectbox('Select a page', ['Pledged Amount by Category', 'Top 20 Country', 'Top 20 Ratio'])

if page == 'Pledged Amount by Category':
    st.header('Pledged Amount by Category')
    data = get_data_top_20_category()
    plot_chart_top_20_category(data)

elif page == 'Top 20 Country':
    st.header('Top 20 Country')
    data = get_data_top_20_country()
    plot_chart_top_20_country(data)

elif page == 'Top 20 Ratio':
    st.header('Top 20 Ratio')
    data = get_data_top_20_ratio()
    plot_chart_top_20_ratio(data)



