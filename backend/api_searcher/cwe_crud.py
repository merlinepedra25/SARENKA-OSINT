from .models import CWEModel, TechnicalImpactModel, CausedByModel, CVEModel


class CWECRUD:
    """
    Klasa odpowiedzialna za operacje bazodanow.
    Jesj zadaniem jest dodanie obiektu CWE do odpowiedniej bazy danych
    """

    def __init__(self, cwe_data):
        self.__cwe_data = cwe_data

    @property
    def cwe_data(self):
        return self.__cwe_data

    @property
    def db_name(self):
        return self.get_database_name()

    def get_database_name(self):
        """Wybiera odpowiednią nazwę bazy danych"""
        if self.cwe_data:
            cwe_id = self.cwe_data["cwe_id"]
            # nazwy baz dancyh to CWE_NONE CWE_79
            return cwe_id.replace("-", "_").upper()

        return "CWE_NONE"  # jawnie ma mi zwrócić, że nie ma  cwe_id

    def add(self):
        """"
        Dodaje obiekt CWE do odpowiedniej bazy danych.
        """
        if self.db_name == "CWE_NONE":
            print("no cwe id")
            cwe_db_obj, is_created = CWEModel.objects.using(self.db_name).get_or_create(
                cwe_id="None",
                title="None",
                description="None",
                likehood="None"
            )

            # jeśli obiekt ZOSTAL WLASNIE stworzony
            # created jest False jak już istnieje w bazie dancyh obiekt
            if is_created:
                TechnicalImpactModel.objects.using(self.db_name).create(
                    title="None",
                    cwe=cwe_db_obj
                )

                CausedByModel.objects.using(self.db_name).create(
                    field="None",
                    process="None",
                    description="None",
                    cwe=cwe_db_obj
                )

