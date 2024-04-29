from abc import ABC, abstractmethod


class AuthMixin:
    is_authenticated = False

    def login(self, senha_tentativa):
        if self.password == senha_tentativa:
            self.is_authenticated = True
            print(f"{self.username} está autenticado")
        else:
            print("Senha incorreta!")

    def logout(self):
        self.is_authenticated = False
        print(f"{self.username} deslogou")


class AbstractAdmin(ABC):
    @abstractmethod
    def login():
        pass

    @abstractmethod
    def logout():
        pass

    @abstractmethod
    def create_content():
        pass

    @abstractmethod
    def update_content():
        pass

    @abstractmethod
    def delete_content():
        pass


class Usuario(AuthMixin):
    role = "Usuário"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nova_senha):
        if isinstance(nova_senha, str):
            if len(nova_senha) >= 8:
                self._password = nova_senha
            else:
                print("O tamanho da senha deve ser >= 8.")
        else:
            print("A senha deve ser uma string.")

    def __repr__(self):
        return f"{self.role}: {self.username}"

    def __eq__(self, outro):
        if isinstance(outro, Usuario):
            return self.username == outro.username

        if isinstance(outro, str):
            return self.username == outro

        return False


class Administrador(Usuario, AbstractAdmin):
    role = "Administrador"

    def create_content(self):
        print(f"{self.username} cria o conteúdo")

    def update_content(self):
        print(f"{self.username} atualiza o conteúdo")

    def delete_content(self):
        print(f"{self.username} deleta o conteúdo")