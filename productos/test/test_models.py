from django.test import TestCase
from productos.models import Telefono, Marca



#Creando nuestros Test aqui

class TelefonoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Telefono.objects.create(nombre='S3',ram='3',procesador='Qualcomm 425',bateria='30080mah',precio='230000')
    
    def test_ram(self):
        telefono=Telefono.objects.get(id=1)
        field_label = telefono._meta.get_field('ram').verbose_name
        self.assertEquals(field_label,'ram')

    def test_nombre(self):
        telefono=Telefono.objects.get(id=1)
        field_label = telefono._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_descripcion(self):
        telefono=Telefono.objects.get(id=1)
        field_label = telefono._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')

    def test_precio(self):
        telefono=Telefono.objects.get(id=1)
        field_label = telefono._meta.get_field('precio').verbose_name
        self.assertEquals(field_label,'precio')
        