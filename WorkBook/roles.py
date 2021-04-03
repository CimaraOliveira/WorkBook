from rolepermissions.roles import AbstractUserRole




class Usuario_Role(AbstractUserRole):
    available_permissions = {
        'permissao_usuario': True,
    }

class Profissional(AbstractUserRole):
    available_permissions = {
        'permissao_profissional': True,
    }