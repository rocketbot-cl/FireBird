# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'FireBird' + os.sep + 'libs' + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

import fdb

# Globals declared here
global mod_firebird_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_firebird_sessions:
        mod_firebird_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_firebird_sessions = {SESSION_DEFAULT: {}}

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "connect":
    dns_ = GetParams('dns_')
    user_ = GetParams('user_')
    pass_ = GetParams('pass_')
    session_ = GetParams('session_')
    var_ = GetParams('var_')

    if not session_:
        session_ = SESSION_DEFAULT
    try:
        con = fdb.connect(
                dsn = dns_,
                user = user_, password = pass_,
                charset='UTF8' # specify a character set for the connection
            )
        cursor = con.cursor()
        mod_firebird_sessions[session_] = {
            "connection": con,
            "cursor": cursor,
            "engine": None,
        }
        
        SetVar(var_,True)
    except Exception as e:
        SetVar(var_,False)
        PrintException()
        raise e     
    
if module == "query":
    query_ = GetParams('query_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]

        # Execute the SELECT statement:
        cursor.execute(query_)
        result = cursor.fetchall()
        SetVar(var_, result)
    except Exception as e:
        SetVar(var_, result)
        PrintException()
        raise e

# if module == "update":
#     query_ = GetParams('query_')
#     var_ = GetParams('var_')
#     session_ = GetParams('session_')

#     if not session_:
#         session_ = SESSION_DEFAULT

#     cursor = mod_firebird_sessions[session_]["cursor"]
#     con = mod_firebird_sessions[session_]["connection"]
    
#     # Execute the UPDATE statement:
#     try:
#         cursor.execute(query_)
#         con.commit()
#         SetVar(var_,True)
#     except:
#         SetVar(var_,False)

if module == "update":
    nombre_ = GetParams('nombre_')
    new_ = GetParams('new_')
    where_ = GetParams('where_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]
        
        if new_[0] == "{":
            new_ = eval(new_)
        if where_[0] == "{":
            where_ = eval(where_)
        
        update = ""
        for k, v in new_.items():
            update += f"{k} = {v} "
        update = update.strip()
        condition = ""
        for k, v in where_.items():
            condition += f"{k} = {v} "  
        condition = condition.strip()
        
        # Execute the UPDATE statement:
        query = f"UPDATE {nombre_} SET {update} WHERE {condition}"
        cursor.execute(query_)
        con.commit()
        SetVar(var_,True)
    except Exception as e:
        SetVar(var_,False)
        PrintException()
        raise e     

if module == "insert":
    nombre_ = GetParams('nombre_')
    colum_ = GetParams('colum_')
    value_ = GetParams('value_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]

        # Execute the INSERT statement:
        
        query = f"INSERT INTO {nombre_} ({colum_}) values({value_})"
        cursor.execute(query)
        con.commit()
    except Exception as e:
        PrintException()
        raise e   

if module == "create":
    nombre_ = GetParams('nombre_')
    campo_ = GetParams('campo_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]

        # Execute the SELECT statement:
        query = f"CREATE TABLE {nombre_} ({campo_})"
        cursor.execute(query)
        con.commit()
    except Exception as e:
        PrintException()
        raise e 

if module == "delete":

    nombre_ = GetParams('nombre_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]

        # Execute the DROP statement:
        cursor.execute("DROP TABLE "+nombre_)
        con.commit()
        SetVar(var_,True)
    except Exception as e:
        SetVar(var_,False)
        PrintException()
        raise e

if module == "select":

    nombre_ = GetParams('nombre_')
    var_ = GetParams('var_')
    session_ = GetParams('session_')

    if not session_:
        session_ = SESSION_DEFAULT

    try:
        cursor = mod_firebird_sessions[session_]["cursor"]
        con = mod_firebird_sessions[session_]["connection"]

        # Execute the SELECT statement:
        query = f"SELECT * FROM {nombre_}"
        cursor.execute(query)
        result = cursor.fetchall()
        SetVar(var_, result)
    except Exception as e:
        SetVar(var_,False)
        PrintException()
        raise e

if module == "close":
    session_ = GetParams('session_')
    
    if not session_:
        session_ = SESSION_DEFAULT

    con = mod_firebird_sessions[session_]["connection"]
    con.close()
    mod_firebird_sessions[session_] = {}