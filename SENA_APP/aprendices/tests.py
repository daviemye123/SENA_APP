from django.test import TestCase, Client
from django.urls import reverse
from aprendices.models import aprendices
from aprendices.forms import AprendizForm
from django.db import IntegrityError


# =============================================================================
# Clase base reutilizable — se define UNA SOLA VEZ
# =============================================================================

class AprendizTestBase(TestCase):
    """Clase base reutilizable que crea un Aprendiz de prueba.
    Heredar de esta clase evita duplicar el setUp en cada TestCase."""

    def setUp(self):
        self.aprendiz = aprendices.objects.create(
            firstname='ranni',
            lastname='lucaria',
            email='ranni@sena.edu.co',
            phone='3101234567',
            cedula='1234567890',
            city='Liurnia de los Lagos',
            date_of_birth='2000-01-15',
            address='Dirección de prueba',
            programa='echisera'
        )
        self.client = Client()


# =============================================================================
# Pruebas del Modelo
# =============================================================================

class AprendizModelTest(AprendizTestBase):

    def test_aprendiz_se_crea_correctamente(self):
        aprendiz = aprendices.objects.get(cedula='1234567890')
        self.assertEqual(aprendiz.firstname, 'ranni')
        self.assertEqual(aprendiz.lastname, 'lucaria')
        self.assertEqual(aprendiz.city, 'Liurnia de los Lagos')

    def test_str_retorna_nombre_y_apellido(self):
        self.assertEqual(str(self.aprendiz), 'ranni lucaria')

    def test_nombre_completo_concatena_correctamente(self):
        self.assertEqual(self.aprendiz.nombre_completo(), 'ranni lucaria')

    def test_documento_identidad_debe_ser_unico(self):
        with self.assertRaises(IntegrityError):
            aprendices.objects.create(
                cedula='1234567890',        # Misma cédula → debe fallar
                firstname='Otro',
                lastname='Usuario',
                email='otro@sena.edu.co',
                phone='3200000000',
                date_of_birth='1995-05-20',
                address='Calle Falsa 123',
                programa='Sistemas'
            )

    def test_campos_opcionales_aceptan_null(self):
        aprendiz_minimo = aprendices.objects.create(
            cedula='9999999999',
            firstname='Maria',
            lastname='Gomez',
            date_of_birth='2001-03-10',
            address='Calle Principal 45',
            programa='Contabilidad'
            # phone, email y city se omiten → deben quedar en None
        )
        self.assertIsNone(aprendiz_minimo.phone)
        self.assertIsNone(aprendiz_minimo.email)
        self.assertIsNone(aprendiz_minimo.city)


# =============================================================================
# Pruebas del Formulario
# =============================================================================

class AprendizFormTest(TestCase):

    def get_datos_validos(self):
        return {
            'cedula': '1098765432',
            'firstname': 'Laura',
            'lastname': 'García',
            'phone': '3209876543',
            'email': 'laura@sena.edu.co',
            'date_of_birth': '2002-07-20',
            'city': 'Medellín',
            'address': 'Calle 50 #10-20',
            'programa': 'ADSO'
        }

    def test_formulario_valido_con_datos_correctos(self):
        form = AprendizForm(data=self.get_datos_validos())
        self.assertTrue(form.is_valid(), msg=f'Errores: {form.errors}')

    def test_documento_con_letras_es_invalido(self):
        datos = self.get_datos_validos()
        datos['cedula'] = 'ABC123456'
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('cedula', form.errors)

    def test_telefono_con_letras_es_invalido(self):
        datos = self.get_datos_validos()
        datos['phone'] = 'abc1234567'
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_telefono_con_menos_de_10_digitos_es_invalido(self):
        datos = self.get_datos_validos()
        datos['phone'] = '31012345'         # Solo 8 dígitos
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_correo_invalido_es_rechazado(self):
        datos = self.get_datos_validos()
        datos['email'] = 'esto_no_es_un_correo'
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_campos_obligatorios_vacios_invalidan_formulario(self):
        form = AprendizForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('cedula', form.errors)
        self.assertIn('firstname', form.errors)
        self.assertIn('lastname', form.errors)


# =============================================================================
# Pruebas de Vistas
# =============================================================================

class AprendizViewsTest(AprendizTestBase):

    # --- Vistas de lectura (GET) ---

    def test_lista_aprendices_responde_200(self):
        url = reverse('aprendices:aprendices_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_lista_aprendices_usa_template_correctoc(self):
        url = reverse('aprendices:aprendices_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'all_aprendices.html')

    def test_lista_aprendices_contiene_el_aprendiz_creado(self):
        url = reverse('aprendices:aprendices_list')
        response = self.client.get(url)
        self.assertContains(response, 'ranni')
        self.assertContains(response, 'lucaria')

    def test_detalle_aprendiz_existente_responde_200(self):
        url = reverse('aprendices:details', args=[self.aprendiz.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1234567890')

    # --- Vistas de escritura (POST) ---

    def test_crear_aprendiz_con_datos_validos_redirige(self):
        url = reverse('aprendices:aprendiz_create')
        datos = {
            'cedula': '5555555555',
            'firstname': 'Carlos',
            'lastname': 'López',
            'phone': '3001112233',
            'email': 'carlos@test.com',
            'date_of_birth': '1999-11-05',
            'city': 'Cali',
            'address': 'Avenida Siempre Viva 123',
            'programa': 'Sistemas'
        }
        response = self.client.post(url, data=datos)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(aprendices.objects.filter(cedula='5555555555').exists())

    def test_crear_aprendiz_con_datos_invalidos_no_redirige(self):
        url = reverse('aprendices:aprendiz_create')
        datos_invalidos = {
            'cedula': 'INVALIDO',
            'firstname': '',
            'lastname': 'Test',
            'date_of_birth': '2000-01-01',
        }
        response = self.client.post(url, data=datos_invalidos)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(aprendices.objects.filter(cedula='INVALIDO').exists())

    def test_editar_aprendiz_actualiza_datos(self):
        url = reverse('aprendices:aprendiz_update', args=[self.aprendiz.id])
        datos_actualizados = {
            'cedula': '1234567890',
            'firstname': 'Rennala',
            'lastname': 'Full Moon',
            'phone': '3009998877',
            'email': 'rennala@rayalucaria.edu.co',
            'date_of_birth': '2000-01-15',
            'city': 'Raya Lucaria',
            'address': 'Gran Biblioteca',
            'programa': 'Hechicería Real'
        }
        response = self.client.post(url, data=datos_actualizados)
        self.assertEqual(response.status_code, 302)
        self.aprendiz.refresh_from_db()
        self.assertEqual(self.aprendiz.firstname, 'Rennala')
        self.assertEqual(self.aprendiz.city, 'Raya Lucaria')

    def test_eliminar_aprendiz_lo_borra_de_la_bd(self):
        aprendiz_id = self.aprendiz.id
        url = reverse('aprendices:aprendiz_delete', args=[aprendiz_id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(aprendices.objects.filter(id=aprendiz_id).exists())


# =============================================================================
# Pruebas de URLs
# =============================================================================

class AprendizURLTest(TestCase):

    def test_url_lista_aprendices_resuelve_correctamente(self):
        url = reverse('aprendices:aprendices_list')
        self.assertEqual(url, '/aprendices/')

    def test_url_crear_aprendiz_resuelve_correctamente(self):
        url = reverse('aprendices:aprendiz_create')
        self.assertEqual(url, '/aprendices/crear/')

    def test_url_detalle_aprendiz_resuelve_correctamente(self):
        url = reverse('aprendices:details', args=[1])
        self.assertEqual(url, '/aprendices/aprendiz/1/')

    def test_url_editar_aprendiz_resuelve_correctamente(self):
        url = reverse('aprendices:aprendiz_update', args=[1])
        self.assertEqual(url, '/aprendices/1/editar/')

    def test_url_eliminar_aprendiz_resuelve_correctamente(self):
        url = reverse('aprendices:aprendiz_delete', args=[1])
        self.assertEqual(url, '/aprendices/1/eliminar/')