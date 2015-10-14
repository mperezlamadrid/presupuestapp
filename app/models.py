from django.db import models

class Rubro(models.Model):
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255)
    budgeted_amount     =models.IntegerField()
    real_amount         =models.IntegerField()
    status              =models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.name

    # def get_name(self):
    #     return selft.__name
    #
    # def get_description(self):
    #     return self.__description
    #
    # def get_budgeted_amount(self):
    #     return self.__budgeted_amount
    #
    # def get_real_amount(self):
    #     return self.__real_amount
    #
    # def get_status(self):
    #     return self.__status
    #
    # def set_name(self, value):
    #     self.__name = value
    #
    # def set_description(self, value):
    #     self.__description = value
    #
    # def set_budgeted_amount(self, value):
    #     self.__budgeted_amount = value
    #
    # def set_real_amount(self, value):
    #     self.__real_amount = value
    #
    # def set_status(self, value):
    #     self.__status = value
    #
    # def get_area(self):
    #     return selft.id_area
    #
    # def mostrarInfo(self):
    #     pass

class Area(models.Model):
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255)
    id_category         =models.IntegerField()

    # def get_name(self):
    #     return self.__name
    #
    # def get_description(self):
    #     return self.__description
    #
    # def set_name(self, value):
    #     self.__name = value
    #
    # def set_description(self, value):
    #     self.__description = value
    #
    # def get_budget_value(self, id_budget):
    #     self.get_budget(id_budget)
    #
    # def get_category(self):
    #     return selft.id_category

class Budget(models.Model):
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255)
    status              =models.CharField(max_length=50)
    id_category         =models.IntegerField()

    # def get_name(self):
    #     return self.__name
    #
    # def get_description(self):
    #     return self.__description
    #
    # def get_status(self):
    #     return self.__status
    #
    # def set_name(self, value):
    #     self.__name = value
    #
    # def set_description(self, value):
    #     self.__description = value
    #
    # def set_status(self, value):
    #     self.__status = value
    #
    # def get_rubros(self):
    #     rubros = []
    #     for r in dir(Rubro):
    #         rubros.push(r)
    #     return rubros
    #
    # def get_total(self, value_rubros):
    #     self.get_rubros()

class Category(models.Model):
    name                =models.CharField(max_length=100)
    status              =models.CharField(max_length=50)

    # def get_name(self):
    #     return self.__name

class Parameter(models.Model):
    pass

class Parameter(models.Model):
    pass
