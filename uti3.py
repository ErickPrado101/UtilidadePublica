import pyodbc

# Função para conectar ao banco de dados
def conn_bd():
    dt_cnt = (
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-T2JV7P5;'
        r'DATABASE=PythonSQL;'
        r'Trusted_Connection=yes;'
    )
    cnt = pyodbc.connect(dt_cnt)
    print("Conexão bem sucedida")
    return cnt

# Função para executar SQL e retornar res em uma lista de tuplas
def exec_sql(conn, cmd):
    curs = conn.cursor()
    curs.execute(cmd)
    res = [row for row in curs.fetchall()]
    return res

# Função para organizar res em uma lista de dicionários
def org_lista_dic(res):
    cols = [column[0] for column in curs.description]
    lis_dic = [dict(zip(cols, row)) for row in res]
    return lis_dic

# Função para organizar res em uma lista de tuplas
def org_lista_tup(res):
    return res

# Função para organizar res em um dicionário
def org_dic(res):
    cols = [column[0] for column in curs.description]
    dic = {row[0]: dict(zip(cols[1:], row[1:])) for row in res}
    return dic

# Função para imprimir res de forma organizada
def imp_res(res):
    for row in res:
        print(row)

# Exibe opções de estruturas de dados
def exi_menu():
    print("Opções:")
    print("1 - Organizar em lista de dicionários")
    print("2 - Organizar em lista de tuplas")
    print("3 - Organizar em dicionário")

def main():
    conn = conn_bd()

    # Exibe menu e obtém opção do usuário
    exi_menu()
    op = input("Digite o número da opção desejada: ")

    cmd = "seu_comando_sql"  # Substitua pelo seu comando SQL real

    res = exec_sql(conn, cmd)

    if op == "1":
        dad_org = org_lista_dic(res)
    elif op == "2":
        dad_org = org_lista_tup(res)
    elif op == "3":
        dad_org = org_dic(res)
    else:
        print("Opção inválida.")
        return

    imp_res(dad_org)
    conn.commit()

if __name__ == "__main__":
    main()
