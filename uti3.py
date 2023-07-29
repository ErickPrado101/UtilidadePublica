import pyodbc

# Função para conectar ao banco
def conn_banco():
    dt_cnt = (
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-T2JV7P5;'
        r'DATABASE=PythonSQL;'
        r'Trusted_Connection=yes;'
    )
    cnt = pyodbc.connect(dt_cnt)
    print("Conexão bem sucedida")
    return cnt

# Função para executar SQL e retornar resultados em uma lista de tuplas
def exec_sql(conn, cmd):
    curs = conn.cursor()
    curs.execute(cmd)
    res = [row for row in curs.fetchall()]
    return res

# Função para imprimir resultados organizados
def imprime_res(res):
    for row in res:
        print(row)

# Opções SQL
def exibe_menu():
    print("Opções:")
    print("1 - Selecionar todos os registros de uma tabela")
    print("2 - Inserir um novo registro em uma tabela")
    print("3 - Atualizar registros em uma tabela")
    print("4 - Deletar registros de uma tabela")
    print("5 - Criar uma nova tabela")
    print("6 - Alterar a estrutura de uma tabela")
    print("7 - Realizar um JOIN em duas tabelas")

def main():
    conn = conn_banco()

    # Exibir menu e obter opção do usuário
    exibe_menu()
    op = input("Digite o número da opção desejada: ")

    if op == "1":
        cmd = "SELECT * FROM sua_tabela"
    elif op == "2":
        cmd = "INSERT INTO sua_tabela (col1, col2) VALUES (val1, val2)"
    elif op == "3":
        cmd = "UPDATE sua_tabela SET col = novo_valor WHERE cond"
    elif op == "4":
        cmd = "DELETE FROM sua_tabela WHERE condicao"
    elif op == "5":
        cmd = "CREATE TABLE nova_tabela (col1 tipo1, col2 tipo2, ...)"
    elif op == "6":
        cmd = "ALTER TABLE sua_tabela ADD col tipo"
    elif op == "7":
        cmd = "SELECT * FROM tabela1 JOIN tabela2 ON tabela1.chave = tabela2.chave"
    else:
        print("Opção inválida.")
        return

    res = exec_sql(conn, cmd)
    imprime_res(res)
    conn.commit()

if __name__ == "__main__":
    main()

