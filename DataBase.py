import pyodbc

pwd = open("psw.txt","r")
pwd = pwd.read()

svr = open("server.txt","r")
svr = svr.read()

dba = open("DBA.txt","r")
dba = dba.read()

class DataBase:
    def __init__(self):
        self.server = str(svr)
        self.database = str(dba)
        self.username = 'suxzaloc'
        self.password = str(pwd)
        self.driver = '{ODBC Driver 17 for SQL Server}'

        try:
            self.cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            self.cursor = self.cnxn.cursor()
        except ValueError:
            print('erro conexão')

    def consulta(self, tabela):
        self.cursor.execute("SELECT * FROM {} ".format(tabela))
        row = self.cursor.fetchone()
        #print(row)
        while row:
            print(row)
            row = self.cursor.fetchone()

    def insert(self,Nome,Idade,DataDeNascimento,Cidade,Estado):
        self.cursor.execute("""INSERT INTO Cliente (Nome, Idade, DataNascimento, Cidade, Estado) VALUES ('{}',{},'{}','{}','{}')""".format(Nome,Idade,DataDeNascimento,Cidade,Estado))
        self.cnxn.commit()

    def updateName(self,valorNome,valorID):
        self.cursor.execute("""UPDATE ODBCProjectPY.dbo.TESTE 
                    SET NOME = '{}' 
                    WHERE ID = {} """.format(str(valorNome),valorID))
        self.cnxn.commit()


