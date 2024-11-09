import streamlit as st

def header(only_image:bool=False):
    if not only_image:
        st.markdown(
        '<div class="image-container">\
        <img src="https://sila.ru/sites/all/themes/sila/images/logo-1.svg"\
        alt="Header Image" width="100" height="100"></div>'
        ,unsafe_allow_html=True
        )
        st.markdown("""
            <style>
                .subheader {
                    padding-top: 20px;
                    font-size: 20px;
                    color: #777;
                    text-align: center;
                    margin-top: -10px;
                }
                .image-container {
                    text-align: center;
                    margin-top: 20px;
                }
            </style>
            <div class="subheader">
                Загрузите файл в формате csv, Excel, или текст обращения напрямую через форму для последующей классификации
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(
        '<div class="image-container">\
        <img src="https://sila.ru/sites/all/themes/sila/images/logo-1.svg"\
        alt="Header Image" width="100" height="100"></div>'
        ,unsafe_allow_html=True
        )
        st.markdown("""
            <style>
                .subheader {
                    padding-top: 20px;
                    font-size: 20px;
                    color: #777;
                    text-align: center;
                    margin-top: -10px;
                }
                .image-container {
                    text-align: center;
                    margin-top: 20px;
                }
            </style>
            <div class="subheader">
                Аналитика по текущим обращениям
            </div>
        """, unsafe_allow_html=True)


def get_color_discrete_sequence():
    return [
            "#0068c9",
            "#83c9ff",
            "#ff2b2b",
            "#ffabab",
            "#29b09d",
            "#7defa1",
            "#ff8700",
            "#ffd16a",
            "#6d3fc0",
            "#d5dae5",
        ]