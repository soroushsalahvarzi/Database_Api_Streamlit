import app_api
import app_db

import streamlit as st

result = tuple()
st.title('THIS APP GET DATA FROM API')
st.sidebar.title('FILTER SECTION')
option = st.sidebar.selectbox('CHOOSE YOUR OPTION',
                ('CALL Movie API', 'INSERT DATA BY USER', 'SELECT ALL RECORDS', 'SELECT BY ID',
                'DELETE BY ID', 'UPDATE BY ID'))
if option == 'CALL Movie API':
    movie_name = st.text_input('Enter movie name: ')
    result = app_api.get_movie_info_by_name(movie_name)
    if st.button('CALL API'):

        st.write(result)
        st.metric('Title', value=result[0])
        st.metric('Year', value=result[1])
        st.metric('Country', value=result[2])
        st.metric('imdb rate', value=result[3])

        st.metric('Genres', value=result[4][0])
        st.success('DATA GET SUCCESSFULLY FROM MOVIE API')
        # print(result)
        # if len(result) > 0:
            # st.checkbox('Insert Data')
    if st.button('ADD Movie INTO DB'):
        app_db.init_db()
        app_db.create_table()
        app_db.insert_movie(result[0], result[1], result[2], result[3], result[4][0])
        st.success('ADD DATA to DATABASE SUCCESSFULLY')
        

elif option == 'SELECT ALL RECORDS':
    result = app_db.select_all_records()
    st.write(result)

elif option == 'SELECT BY ID':
    id = st.number_input('Enter movie id', min_value=1)
    result = app_db.select_record_by_id(id)
    st.write(result)

elif option == 'DELETE BY ID':
    id = st.text_input('Enter movie id')
    if st.button('DELETE'):
        app_db.delete_record_by_id(id)
        st.success(f'record by id {id} delete successfully')
        result = app_db.select_all_records()
        st.write(result)

elif option == 'UPDATE BY ID':
    id = st.text_input('enter movie id')
    result = app_db.select_record_by_id(id)
    st.write(result)
    year = st.text_input('enter year of movie: ')
    imdb_rate = st.text_input('enter imdb_rate: ')
    app_db.update_record_by_id(id, year, imdb_rate)
    if st.button('UPDATE'):
        result = app_db.select_record_by_id(id)
        st.write(result)
