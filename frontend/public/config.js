// Configurações do Frontend - Chatbot IA
// Este arquivo pode ser usado para configurações específicas do frontend

const FRONTEND_CONFIG = {
  // URLs padrão (fallback caso não consiga carregar do backend)
  DEFAULT_URLS: {
    backend_base_url: 'http://localhost:5000',
    backend_chat_url: 'http://localhost:5000/chat', 
    backend_personalities_url: 'http://localhost:5000/personalities',
    backend_config_url: 'http://localhost:5000/config'
  },
  
  // Configurações da interface
  UI: {
    typing_indicator: '<i>Digitando...</i>',
    error_message: 'Erro ao se comunicar com o servidor.',
    loading_message: 'Erro ao carregar IAs',
    new_session_message: '<i>Nova sessão selecionada.</i>'
  },
  
  // Configurações de comportamento
  BEHAVIOR: {
    auto_scroll: true,
    save_session_to_localStorage: true,
    default_personality: 'nutricionista'
  }
};

// Função para obter as configurações de URL
async function getApiUrls() {
  try {
    const response = await fetch(FRONTEND_CONFIG.DEFAULT_URLS.backend_config_url);
    if (response.ok) {
      const config = await response.json();
      console.log('✓ Configurações carregadas do backend:', config);
      return config;
    }
  } catch (error) {
    console.warn('⚠ Erro ao carregar configurações, usando URLs padrão:', error);
  }
  
  // Retorna URLs padrão em caso de erro
  return FRONTEND_CONFIG.DEFAULT_URLS;
}
