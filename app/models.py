from django.db import models

class Area(models.Model):
    DEFAULT_ID = 1
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255,blank=True)
    status              =models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)

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

class Rubro(models.Model):
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255,blank=True)
    budgeted_amount     =models.IntegerField()
    real_amount         =models.IntegerField()
    status              =models.CharField(max_length=50)
    area                =models.ForeignKey('Area',default=Area.DEFAULT_ID)

    def __unicode__(self):
        return '%s' % (self.name)

    def get_area(self):
        return '%s' % (self.area)

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

class Budget(models.Model):
    name                =models.CharField(max_length=100)
    description         =models.CharField(max_length=255,blank=True)
    status              =models.CharField(max_length=50)
    rubro               =models.ManyToManyField(Rubro)

    def rubros(self):
        return "\n".join([p.name+", " for p in self.rubro.all()])

    def total(self):
        sum_total = 0
        for p in self.rubro.all():
            sum_total = sum_total + p.real_amount
        return sum_total

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

class Parameter(models.Model):
    attribute               =models.CharField(max_length=50)
    description             =models.CharField(max_length=200)
    status_parameter        =models.CharField(max_length=1)

    def __str__(self):
        return self.attribute


class ValueParameter(models.Model):
    value                       =models.CharField(max_length=30)
    parameter                   =models.ForeignKey('Parameter')
    order                       =models.CharField(max_length=3)
    status_value_parameter      =models.CharField(max_length=1)


    def __str__(self):
        return self.value
