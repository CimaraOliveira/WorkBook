from rolepermissions.roles import AbstractUserRole




class Usuario(AbstractUserRole):
    available_permissions = {
        'permissao_usuario': True,
    }

class Profissional(AbstractUserRole):
    available_permissions = {
        'permissao_profissional': True,
    }