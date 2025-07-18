import streamlit as st

st.title('AI Risk Radar')
st.write('Upload your project document to analyze risks.')

uploaded_file = st.file_uploader('Choose a file', type=['pdf', 'docx', 'txt'])
if uploaded_file:
    st.success(f'File {uploaded_file.name} uploaded successfully!')
    st.write('Analyzing risks... (future feature)')

