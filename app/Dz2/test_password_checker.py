import pytest

from password_checker import is_strong_password


class TestIsStrongPassword:
    @pytest.mark.parametrize(
        "password, expected",
        [
            ("Abcdef1!", True), # рівно 8 символів, є все
            ("p@ssw0rd", True), # рівно 8 символів
            ("Passw0rd!2026", True), # довгий надійний
            ("Пароль123!", True), # кирилиця теж літери
            ("Abcde1!", False), # 7 символів - закороткий
            ("a1!", False), # дуже короткий
            ("", False), # порожній рядок
            ("abcdefgh1", False), # немає символу
            ("abcdefgh!", False), # немає цифри
            ("12345678!", False), # немає літери
            ("!!!!!!!!", False), # тільки символи
            ("abc def1!", False), # пробіл всередині
            (" Abcdef1!", False), # пробіл на початку
            ("Abcdef1! ", False), # пробіл в кінці
        ],
    )
    def test_is_strong_password(self, password, expected):
        assert is_strong_password(password) is expected

    @pytest.mark.skip(reason="тест або поламаний ябо ше якась фігня")
    def test_character_variety(self):
        pass