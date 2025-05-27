import pytest
import json
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    """Cria um cliente de teste Flask"""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    with app.test_client() as client:
        with app.app_context():
            yield client

class TestChatEndpoint:
    """Testes para o endpoint /chat"""
    
    def test_chat_sem_mensagem(self, client):
        """Testa quando não é fornecida uma mensagem"""
        response = client.post('/chat', 
                             json={},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['error'] == 'Mensagem não fornecida'
    
    def test_chat_mensagem_vazia(self, client):
        """Testa quando é fornecida uma mensagem vazia"""
        response = client.post('/chat', 
                             json={'message': ''},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['error'] == 'Mensagem não fornecida'
    
    @patch('app.requests.post')
    def test_chat_sucesso(self, mock_post, client):
        """Testa uma requisição de chat bem-sucedida"""
        # Mock da resposta da API do Groq
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Olá! Como posso ajudá-lo com suas necessidades nutricionais hoje?'
                }
            }]
        }
        mock_post.return_value = mock_response
        
        response = client.post('/chat', 
                             json={'message': 'Olá, preciso de ajuda com minha dieta'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
        assert 'session_id' in data
        assert data['response'] == 'Olá! Como posso ajudá-lo com suas necessidades nutricionais hoje?'
    
    @patch('app.requests.post')
    def test_chat_com_session_id(self, mock_post, client):
        """Testa chat fornecendo um session_id específico"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Resposta do assistente nutricional'
                }
            }]
        }
        mock_post.return_value = mock_response
        
        test_session_id = 'test-session-123'
        response = client.post('/chat', 
                             json={
                                 'message': 'Qual é a melhor dieta para perda de peso?',
                                 'session_id': test_session_id
                             },
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['session_id'] == test_session_id
    
    @patch('app.requests.post')
    def test_chat_erro_api_groq(self, mock_post, client):
        """Testa quando a API do Groq retorna erro"""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = 'Internal Server Error'
        mock_post.return_value = mock_response
        
        response = client.post('/chat', 
                             json={'message': 'Teste de erro'},
                             content_type='application/json')
        
        assert response.status_code == 500
        data = json.loads(response.data)
        assert data['error'] == 'Erro na chamada da IA'
        assert 'details' in data
    
    @patch('app.requests.post')
    def test_chat_nova_sessao_vazia(self, mock_post, client):
        """Testa criação de nova sessão com session_id vazio"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Nova sessão criada!'
                }
            }]
        }
        mock_post.return_value = mock_response
        
        response = client.post('/chat', 
                             json={
                                 'message': 'Começar nova conversa',
                                 'session_id': ''
                             },
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'session_id' in data
        assert data['session_id'] != ''
    
    def test_chat_metodo_nao_permitido(self, client):
        """Testa tentativa de usar método GET no endpoint /chat"""
        response = client.get('/chat')
        assert response.status_code == 405  # Method Not Allowed
    
    @patch('app.requests.post')
    def test_chat_verifica_payload_groq(self, mock_post, client):
        """Testa se o payload enviado para o Groq está correto"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Resposta do assistente'
                }
            }]
        }
        mock_post.return_value = mock_response
        
        client.post('/chat', 
                   json={'message': 'Teste de payload'},
                   content_type='application/json')
        
        # Verifica se a chamada foi feita com os parâmetros corretos
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        
        # Verifica headers
        headers = call_args[1]['headers']
        assert 'Authorization' in headers
        assert headers['Content-Type'] == 'application/json'
        
        # Verifica payload
        payload = call_args[1]['json']
        assert 'model' in payload
        assert 'messages' in payload
        assert 'max_tokens' in payload
        assert 'temperature' in payload
        assert payload['max_tokens'] == 512
        assert payload['temperature'] == 0.7

if __name__ == '__main__':
    pytest.main([__file__])