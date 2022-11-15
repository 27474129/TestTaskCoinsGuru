from postgresql.postgresql import Postgresql


class UserModelRepository:
    @staticmethod
    def add_user(user_data) -> None:
        Postgresql.execute_single_query(f"INSERT INTO users (firstname, secondname, email, password) \
        VALUES ('{user_data.firstname}', '{user_data.secondname}', '{user_data.email}', '{user_data.password}');")

    @staticmethod
    def check_by_email_if_user_exists(email: str) -> bool:
        return True if type(Postgresql.execute_single_query(f"SELECT * FROM users WHERE email='{email}';")) \
                       is not bool else False

    @staticmethod
    def change_email(user_id: int, new_email: str) -> None:
        Postgresql.execute_single_query(f"UPDATE users SET email='{new_email}' WHERE id='{user_id}';")
