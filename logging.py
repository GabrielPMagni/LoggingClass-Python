
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
            self.default_levels = [{'level': 0, 'msg': 'INFO::\tDATE:{date}\tMSG:{pattern_text}'}, {'level': 1, 'msg': 'WARN::\tDATE:{date}\tMSG:{pattern_text}'}, {'level': 2, 'msg': 'ERROR::\tDATE:{date}\tMSG:{pattern_text}'}, {'level': 3, 'msg': 'FORBBIDEN::\tDATE:{date}\tMSG:{pattern_text}'}]
            self.accepted_levels = self.default_levels
            return {'result': 0, 'msg': 'Arquivo configurado'}
        except PermissionError:
            return {'result': 1, 'msg': 'Permissão ao arquivo negada.'}
        except Exception as e:
            return {'result': 9, 'msg': f'Erro não tratado: {e}'}

    def new_level(self, description: str, level: int) -> dict:
        '''
        Insere novos níveis de logs customizados
        '''
        try:
            if (description.strip() == ''):
                return {'result': 21, 'msg': 'Descrição inválida para novo nível de log.'}
            else:
                description = description.strip()
            for i in range(len(self.accepted_levels)):
                if (self.accepted_levels[i]['level'] == level): return {'result': 22, 'msg': 'Nível de log já utilizado.'}
            date = 'date'  # Usado para permitir inclusão na formatação do pattern
            pattern_text = 'pattern_text'
            level_pattern = f'{description}::\tDATE:{date}\tMSG:{pattern_text}'
            self.accepted_levels.append({'level': level, 'msg': level_pattern})
            return {'result': 0, 'msg': 'Novo nível de log inserido com sucesso.'}
        except Exception as e:
            return {'result': 29, 'msg': f'Erro não tratado: {e}'}
    
    def __insert_to_file(self, text: str) -> dict:
        '''
        Método privado para inserir dados ao logs após serem tratados
        '''
        try:
            self.log_file = open(self.log_file_name, 'a')
            self.log_file.write(text)
            self.log_file.close()
            return {'result': 0, 'msg': 'Dado inserido'}
        except PermissionError:
            return {'result': 11, 'msg': 'Permissão ao arquivo negada.'}
        except Exception as e:
            return {'result': 19, 'msg': f'Erro não tratado: {e}'}

    def log(self, text: str, level: int) -> dict:
        '''
        Método para realizar o log com base no nível e mensagem de parâmetro
        '''
        log_errors = ''
        template = ''
        try:
            if (level not in self.accepted_levels): log_errors += 'Nível de erro não implementado'
            if text == '': log_errors += 'Mensagem para log inválida'
            if log_errors != '': raise Exception(log_errors)
            self.__insert_to_file(template)
        except Exception as e:
            return {'result': 39, 'msg': f'Erro não tratado: {e}'}
            
