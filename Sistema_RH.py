#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date
import pandas as pd


# In[ ]:


class Funcionarios:
    def __init__(self):
        self.id_func = 0
        self.nome = ''
        self.sobrenome = ''
        self.data_admissao = ''
        
        
    #Fases do Recrutamento
    def SelecaoExterna(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    
    #1ª etapa do processo
    def Dinamica(self):
        print(f'Nome do candidato: {self.nome} {self.sobrenome}')
        try:
            self.dinamica = input('Candidato passou na dinâmica? ')
            try:
                if self.dinamica == 'sim' or dinamica == 's':
                    print('Candidato apto para proxima etapa')
            except:
                print('Candidado não está apto para próxima etapa')
        except:
            print('Siga a ordem de testes parar contratação')

            
    #2ª etapa do processo       
    def Entrevista(self):
        try:
            if self.dinamica == 'sim':
                self.entrevista = input('Candidato passou na entrevista? ')
                if self.entrevista == 'sim':
                    print('Candidato apto para proxima etapa')
                else:
                    print('Candidado não está apto para próxima etapa')
        except:
            print('Siga a ordem de testes parar contratação')
            
      
    #3ª etapa do processo
    def Pratica(self):
        try:
            if self.dinamica == 'sim':
                if self.entrevista == 'sim':
                    self.pratica = input('Candidato passou na prática? ')
                    if self.pratica == 'sim':
                        print('Candidato apto para ser contratado')
                    else:
                        print('Candidado não está apto para próxima etapa')
        except:
            print('Siga a ordem de testes parar contratação')
            
            
    def Contratar(self, id_func, data_admissao, salario):
        try:
            if self.dinamica == 'sim':
            if self.entrevista == 'sim':
                    if self.pratica == 'sim':
                        self.id_func = id_func
                        self.data_admissao = data_admissao
                        self.salario = float(salario)
                        print(f'Você acaba de contratar {self.nome} {self.sobrenome} \nID do funcionário: {self.id_func} \nData de admissão: {self.data_admissao} \nSalário: R${self.salario:.2f}')
                        dados_contratados.append([self.nome, self.sobrenome, self.id_func, self.data_admissao, self.salario])
                        dados_contratados = pd.DataFrame(dados_contratados, columns=['Nome', 'Sobrenome', 'ID Funcionário', 'Data de Admissão', 'Salário'])
                        dados_contratados.to_excel('Dados_Contratados.xlsx', index=False)
        except:
                    print('Siga a ordem de testes parar contratação')
        
    
    #Recrutamento Interno
    def SelecaoInterna(self):
        try:
            self.data_admissao = datetime.strptime(self.data_admissao, '%d/%m/%Y').date()
            tempo_necessario = date.today() - self.data_admissao
            print(self.data_admissao)
            self.resposta = input(f'Nome do funcionário: {self.nome} {self.sobrenome} \nO funcionário possui o tempo necessário para promoção? {tempo_necessario}')
            if self.resposta == 'sim':
                self.qualificacoes = input('O funcionário possui as qualificações exigidas? ')
                if self.qualificacoes == 'sim':
                    self.salario = input('Informe novo salário do funcionário R$')
                else:
                    print('O funcionário não possui os requisitos necessários para promoção')
            else:
                print('O funcionário não possui os requisitos necessários para promoção')
        except:
            print('Funcionário não existe no banco de dados')


# In[ ]:


funcionario1 = Funcionarios()
funcionario1.SelecaoExterna('Fulano', 'Tal')
funcionario1.Dinamica()
funcionario1.Entrevista()
funcionario1.Pratica()
funcionario1.Contratar(123, '08/02/2021', 1000)
# funcionario1.SelecaoInterna()

funcionario2 = Funcionarios()
funcionario2.SelecaoExterna('Ciclano', 'Silva')
funcionario2.Dinamica()
funcionario2.Entrevista()
funcionario2.Pratica()
funcionario2.Contratar(456, '25/01/2022', 1100)
# funcionario2.SelecaoInterna()

