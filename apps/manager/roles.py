from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'acessar_produtos':True,
        'adicionar_produtos':True,
        'deletar_produtos':True,
        'modificar_produtos':True}
    

class Usuario(AbstractUserRole):
    available_permissions = {
        'acessar_produtos':True
    }
    