import React, { useState } from 'react';
import useApiConfig from '../hooks/useApiConfig';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const { config: apiConfig, loading: configLoading, error: configError } = useApiConfig();

  const sendMessage = async () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: 'Você', text: input }]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(apiConfig.backend_chat_url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      const data = await response.json();
      setMessages(msgs => [...msgs, { sender: 'IA', text: data.response || data.resposta || 'Sem resposta' }]);
    } catch (error) {
      setMessages(msgs => [...msgs, { sender: 'IA', text: 'Erro ao se comunicar com o servidor.' }]);
    }
    setLoading(false);
  };

  if (configLoading) {
    return (
      <div className="bg-white rounded shadow-md p-6 w-96">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="sr-only">Carregando configurações...</span>
          </div>
          <p>Carregando configurações...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded shadow-md p-6 w-96">
      <div className="mb-4 h-64 overflow-y-auto border-b">
        {messages.map((msg, idx) => (
          <div key={idx} className={`my-2 text-${msg.sender === 'Você' ? 'right' : 'left'}`}>
            <b>{msg.sender}: </b>{msg.text}
          </div>
        ))}
        {loading && <div>Carregando...</div>}
      </div>
      <div className="flex">
        <input
          className="flex-1 border rounded px-2 py-1"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && sendMessage()}
          placeholder="Digite sua mensagem..."
        />
        <button
          className="ml-2 px-4 py-1 bg-blue-500 text-white rounded"
          onClick={sendMessage}
          disabled={loading}
        >
          Enviar
        </button>
      </div>
    </div>
  );
}

export default Chat;