from flask.wrappers import Response
from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True #ambiente de testing
        app.config['WTF_CSRF_ENABLED'] = False #crosside request desactivado,
        return app #se retorna la app


    def test_app_exists(self):  # comprobar que la app existe.
        self.assertIsNotNone(current_app) #la app que está en este momento (importada)

    def test_app_in_test_mode(self): #comprobar si la app está en modo test.
        self.assertTrue(current_app.config['TESTING'])    

    def test_index_redirect(self):
        response = self.client.get(url_for('index')) #client se refiere al navegador
        self.assertRedirects(response,url_for('hello')) #

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login')) #primero vamos al blueprint y luego a la ruta login 

        self.assert200(response)


    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))  

        self.assertTemplateUsed('login.html') #comprovamos que el template se renderiza, solo se le tiene que enviar el nombre del template.   


    def test_auth_login_post(self):
        fake_form = {
            'user_name': 'fake',
            'password': 'fake-password'
        }

        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))