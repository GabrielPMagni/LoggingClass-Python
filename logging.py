
class Logging:
    '''
    Registra no arquivo de log definido no construtor o que ocorreu (parâmetro) com o nível de prioridade.\n
    0 = Informativo; 
    1 = Avisos; 
    2 = Erros; 
    3 = Ação não permitida;
    '''

    # Constantes
    INFO=0
    WARN=1
    ERROR=2
    FORBBIDEN=3

    def __init__(self, log_file_name: str) -> dict:
        try:
            self.log_file = open(log_file_name, 'a')  # Testa acesso ao arquivo
            self.log_file_name = log_file_name  # Atribui o nome do arquivo caso funcione acesso
            self.log_file.close()  # Fecha o acesso. Será reaberto somente se necessário
            return {'result': 0, 'msg': 'Arquivo configurado'}
        except PermissionError:
            return {'result': 1, 'msg': 'Permissão ao arquivo negada.'}
        except Exception as e:
            return {'result': 100, 'msg': f'Erro não tratado: {e}'}

    
    def __insert_to_file(self, text: str) -> bool:
        '''
        Método privado para inserir dados ao logs após serem tratados
        '''
        try:
            self.log_file = open(self.log_file_name, 'a')
            self.log_file.write(text)
            self.log_file.close()
            return {'result': 0, 'msg': 'Dado inserido'}
        except PermissionError:
            return {'result': 1, 'msg': 'Permissão ao arquivo negada.'}
        except Exception as e:
            return {'result': 100, 'msg': f'Erro não tratado: {e}'}

    def log(self, text: str, level: int) -> dict:
        pass