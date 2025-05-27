import React from 'react';
import useApiConfig from '../hooks/useApiConfig';

/**
 * Componente que exibe o status das configurações da API
 * Útil para debug e verificação do sistema
 */
function ConfigStatus() {
  const { config, loading, error, isConfigLoaded, reloadConfig } = useApiConfig();

  const getStatusColor = () => {
    if (loading) return 'text-yellow-600';
    if (error) return 'text-red-600';
    if (isConfigLoaded) return 'text-green-600';
    return 'text-gray-600';
  };

  const getStatusIcon = () => {
    if (loading) return '🔄';
    if (error) return '❌';
    if (isConfigLoaded) return '✅';
    return '⚪';
  };

  const getStatusText = () => {
    if (loading) return 'Carregando configurações...';
    if (error) return `Erro: ${error}`;
    if (isConfigLoaded) return 'Configurações carregadas com sucesso';
    return 'Status desconhecido';
  };

  return (
    <div className="bg-gray-100 border rounded p-3 mb-4 text-sm">
      <div className="flex items-center justify-between mb-2">
        <div className={`flex items-center ${getStatusColor()}`}>
          <span className="mr-2">{getStatusIcon()}</span>
          <span className="font-medium">{getStatusText()}</span>
        </div>
        <button
          onClick={reloadConfig}
          disabled={loading}
          className="px-2 py-1 text-xs bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
          title="Recarregar configurações"
        >
          {loading ? '🔄' : '🔄 Reload'}
        </button>
      </div>
      
      {isConfigLoaded && (
        <div className="text-xs text-gray-600 space-y-1">
          <div><strong>Base URL:</strong> {config.backend_base_url}</div>
          <div><strong>Chat URL:</strong> {config.backend_chat_url}</div>
          <div><strong>Personalities URL:</strong> {config.backend_personalities_url}</div>
        </div>
      )}
      
      {error && (
        <div className="text-xs text-red-600 mt-2">
          <strong>Usando configurações padrão:</strong>
          <div>• Base URL: http://localhost:5000</div>
          <div>• Chat URL: http://localhost:5000/chat</div>
          <div>• Personalities URL: http://localhost:5000/personalities</div>
        </div>
      )}
    </div>
  );
}

export default ConfigStatus;
