import streamlit as st
from index_now import IndexNow


def main():
    st.title('🚀 Index Now')

    with st.form(key='index_form'):
        host = st.text_input('Host')
        key = st.text_input('Key')
        urls = st.text_area('Enter URLs, one per line')
        submit_button = st.form_submit_button(label='Index Now')

    if submit_button:
        indexing = IndexNow(host=host, key=key)
        status_code, response_text, reason_text = indexing.index_now(urls.split('\n'))
        st.write(f'Status code: {status_code}')
        # st.write('Response:')
        # st.write(response_text)
        st.write(f'Reason: {reason_text}')


if __name__ == '__main__':
    main()