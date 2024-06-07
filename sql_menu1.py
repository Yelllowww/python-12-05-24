import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1')
    print('Conexão_db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = '''CREATE DATABASE if not exists db_loja_3'''
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print("\nConexão fechada")

def create_connection():
    conexao = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1',
                                        database='db_loja_3')
    print('Conexão:', conexao)
    return conexao

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada')

def create_table():
    tabela = '''CREATE TABLE if not exists produto(
                identificador INTEGER NOT NULL AUTO_INCREMENT,
                nome CHAR(50),
                preco DECIMAL(9,2) NOT NULL,
                dt_validade DATE NOT NULL,
                PRIMARY KEY (identificador))'''

    tabela2 = '''CREATE TABLE funcionario(
                matricula INTEGER NOT NULL AUTO_INCREMENT,
                nome CHAR(50),
                dt_matricula DATE,
                salario DECIMAL(6,2),
                PRIMARY KEY (matricula)'''
    cursor.execute(tabela)
    cursor.execute(tabela2)

def insert_table():
    insere_preco = float(input("Digite o preço:"))
    insere_nome = input("Digite o nome do funcionário:")
    sql = f'''INSERT INTO produto (nome,preco,dt_validade) 
            VALUES('leite',{insere_preco},'2024-05-29')'''

    sql2 = f'''INSERT INTO funcionario 
            (nome,dt_matricula,salario) VALUES(
            {insere_nome},'2024-05-28',1900)'''
    cursor.execute(sql)
    conexao.commit()
    cursor.execute(sql2)
    conexao.commit()

def select_all():
    registros = cursor.fetchall()
    for i in registros:
        print(i)
if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    while True:
        print("\nMenu:")
        print("1. Digite 1 para inserir tabelas.")
        print("2. Digite 2 para ver todos os registros.")
        print("3. Digite 3 para sair.")
        num = int(input())
        if num == 1:
            insert_table()
        elif num == 2:
            select_all()
        elif num == 3:
            break
        else:
            print("Número inválido")
    close_connection()