import streamlit as st

def kali_kalian_def(): 
    if kali_kalian == "+":
        st.success(f"Hasil {input_num1 + input_num2}")
    elif kali_kalian == "x":
        st.success(f"Hasil {input_num1 * input_num2}")
    elif kali_kalian == "-":
        st.success(f"Hasil {input_num1 - input_num2}")
    elif kali_kalian == "/":
        st.success(f"Hasil {input_num1 / input_num2}")

st.title(body="Calculator")
input_num1=  st.number_input(label="Masukan angka1: ", value=0)
kali_kalian= st.selectbox(
    "Pilih",
    ("+", "x", "-", "/")
)
input_num2=  st.number_input(label="Masukan angka2: ", value=0)
st.header(body="\n")
button = st.button(label="Submit")
if button:
    kali_kalian_def()
