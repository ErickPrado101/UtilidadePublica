import pyodb

dt_cnt = (
    Driver={SQL Server}; 
    Server = DESTOP- T2JV7P5;
    Database = PythonSQL;
)

cnt = pyodbc.connect(dt_cnt)
print("Conexão bem sucedida")
curs=cnt.cursor()

info_cmd = []

cmd = " "

curs.execute(cmd)

curs.commit()
