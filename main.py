import streamlit as st
from index_now import IndexNow


def main():
    st.title('🚀 Index Now')

    # map the user-friendly display values to the actual values for searchengines
    type_mapping = {
        'Yandex': 'yandex.com',
        'Bing': 'www.bing.com'
    }

    with st.form(key='index_form'):
        host = st.text_input('Host')

        key = st.text_input('Key')

        # Get the user's selection from the app
        select_searchengine = st.selectbox('Select searchengine',['Yandex', 'Bing'], index=False)
        searchengine = type_mapping[select_searchengine]

        urls = st.text_area('Enter URLs, one per line')
        submit_button = st.form_submit_button(label='Index Now')

    if submit_button:
        indexing = IndexNow(host=host, key=key, searchengine=searchengine)
        status_code, response_text, reason_text = indexing.index_now(urls.split('\n'))
        st.write(f'Status code: {status_code}')
        # st.write('Response:')
        # st.write(response_text)
        st.write(f'Reason: {reason_text}')

    st.markdown('🔍 [What is IndexNow?](https://www.indexnow.org/)')
    st.markdown('📖 [Documentation](https://www.indexnow.org/documentation)')


if __name__ == '__main__':
    main()