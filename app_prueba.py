# Importancion de librerias:
import pandas as pd
import numpy as np
import streamlit as st
import streamlit_authenticator as stauth
import sqlite3 as sql
import time

# Algunas funciones:

def lectura_bbdd(query):
    
    conn = sql.connect('etiquetado_streamlit.db')
    cursor = conn.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    
    return datos


def insertar_usuario(name, username, password):
    
    conn = sql.connect('etiquetado_streamlit.db')
    cursor = conn.cursor()
    query = '''
    INSERT INTO usuarios (name, username, password, master) VALUES ('{}', '{}', '{}', 0)
    '''.format(name, username, password)
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    return None

# Aplicacion

placeholder = st.empty()

with placeholder.container():
    
    st.title('Hola esto es una prueba')
    
    menu = ['Home', 'Login', 'SignUp']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Esto es una app que tal tal tal ')
        
    elif choice == 'Login':
        st.subheader('Sección de Login')
        
        username = st.text_input('Usuario')
        password = st.text_input('Contraseña', type = 'password')
        
        if st.button('Login'):
            
            usuarios_pre = lectura_bbdd('SELECT username FROM usuarios')
            usuarios = [x[0] for x in usuarios_pre]
            
            if username in usuarios:
                
                password_correcta = lectura_bbdd('''SELECT password FROM usuarios WHERE username = \'{}\''''.format(username))
                
                if password == password_correcta[0][0]:
                    st.success('Logged in as {}'.format(username))
                    time.sleep(1.1)
    
                    placeholder.empty()
                    placeholder.title('Etiquetado de connsultas del buzón')
                    
                    ##############################
                    
                    ### Aqui va la APP
                    
                                  
                    #################################     
                    
                    
        
                else:
                    st.warning('Usuario o contraseña incorrectos')
            else:
                st.warning('El usuario no existe en la base de datos')
        
    elif choice == 'SignUp':
        st.subheader('Crear una nueva cuenta')
        
        new_user = st.text_input('Nuevo Usuario')
        new_password = st.text_input('Nueva Contraseña', type = 'password')
        ref_number = st.text_input('Código de invitación')
        
        if st.button('Sign Up'):
            
            usuarios_pre = lectura_bbdd('SELECT username FROM usuarios')
            usuarios = [x[0] for x in usuarios_pre]
            
            ref_code_pre = lectura_bbdd('SELECT ref_code FROM usuarios')
            ref_codes = [x[0] for x in ref_code_pre]
            
            if (ref_number in ref_codes) & (new_user not in usuarios):
                insertar_usuario('Nombre', new_user, new_password)
                st.success('Usuario dado de alta correctamente')
                st.info('Accede al menu de Login para entrar a la aplicación')
            
            else:
                st.warning('Numero de referencia incorrecto o el usuario ya existe. No se puede dar de alta el usuario')
            





# names = ['alvaro', 'bea']
# usernames = ['alvarosooli', 'beabea']
# passwords = ['1234a', '1234b']
# hashed_passwords = stauth.Hasher(passwords).generate()

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'aaa', 'ssss', cookie_expiry_days=23)
# name, authenticaton_status, username = authenticator.login('Login', 'main')

# if authenticaton_status == False:
#     st.error("Usuario o contraseña incorrectos")
# if authenticaton_status == None:
#     st.warning('Por favor introduce tu usuario y contraseña')
# if authenticaton_status:
#     print('Has entrado!!!!')