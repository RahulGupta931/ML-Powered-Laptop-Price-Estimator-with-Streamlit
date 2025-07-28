import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('laptop.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")
st.markdown("Get an estimated price for your laptop configuration")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Specifications")
    # brand
    company = st.selectbox('Brand', df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type', df['TypeName'].unique())

    # Ram
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # weight
    weight = st.number_input('Weight of the Laptop (kg)',
                             min_value=0.5, max_value=5.0, value=2.0, step=0.1)

    # cpu
    cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

    # os
    os = st.selectbox('Operating System', df['OS'].unique())

with col2:
    st.subheader("Display & Storage")
    # Touchscreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

    # screen size
    screen_size = st.slider('Screen size in inches', 10.0, 18.0, 13.0)

    # resolution
    resolution = st.selectbox('Screen Resolution', [
                              '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

    # storage
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

    # gpu
    gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

st.markdown("---")
if st.button('🔮 Predict Price', type="primary"):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company, type, ram, weight, touchscreen,
                     ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)
    result = np.exp(pipe.predict(query))

    st.success(
        f"The predicted price of this configuration is ${result[0]:,.2f}")
