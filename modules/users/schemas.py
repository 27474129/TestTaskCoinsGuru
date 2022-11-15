import re
from pydantic import BaseModel, validator
from .repository import UserModelRepository


class UserModel(BaseModel):
    firstname: str
    secondname: str
    email: str
    password: str


class UserCreationModel(UserModel):
    password2: str

    @staticmethod
    def __get_letters_and_digits_count(value: str) -> list:
        result = []
        result.append(len(re.findall(r"[а-я]", value)))
        result.append(len(re.findall(r"[А-Я]", value)))
        result.append(len(re.findall(r"[a-z]", value)))
        result.append(len(re.findall(r"[A-Z]", value)))
        result.append(len(re.findall(r"[0-9]", value)))
        return result

    @validator("firstname")
    def validate_firstname(cls, firstname: str):
        errors = []
        if len(firstname) < 2:
            errors.append("Имя должно содержать минимум 2 символа")
        if len(firstname) > 15:
            errors.append("Имя не должно содержать больше 15 символов")

        letters_and_digits_count = UserCreationModel.__get_letters_and_digits_count(firstname)
        if letters_and_digits_count[-1] != 0:
            errors.append("Имя должно содержать только русские и/или английские буквы")

        if len(errors) != 0:
            raise ValueError(errors)

        return firstname

    @validator("secondname")
    def validate_secondname(cls, secondname: str):
        errors = []
        if len(secondname) < 2:
            errors.append("Фамилия должно содержать минимум 2 символа")
        if len(secondname) > 20:
            errors.append("Фамилия не должно содержать больше 20 символов")

        letters_and_digits_count = UserCreationModel.__get_letters_and_digits_count(secondname)
        if letters_and_digits_count[-1] != 0:
            errors.append("Фамилия должна содержать только русские и/или английские буквы")

        if len(errors) != 0:
            raise ValueError(errors)

        return secondname

    @validator("email")
    def validate_email(cls, email: str):
        errors = []

        if UserModelRepository.check_by_email_if_user_exists(email):
            errors.append("Email занят!")

        if len(errors) != 0:
            raise ValueError(errors)

        return email

    @validator("password")
    def validate_password(cls, password: str):
        errors = []
        if len(password) < 6:
            errors.append("Пароль должен содержать минимум 6 символов")

        letters_and_digits_count = UserCreationModel.__get_letters_and_digits_count(password)
        if letters_and_digits_count[-1] == 0:
            errors.append("Пароль должен содержать минимум одну цифру")

        if len(errors) != 0:
            raise ValueError(errors)

        return password
