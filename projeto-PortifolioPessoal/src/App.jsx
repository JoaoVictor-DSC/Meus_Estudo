import { useState } from 'react'
import './App.css'
import Header from './components/header'
import Portfolio from './components/Portfolio'
import Footer from './components/footer'

function App() {
  // O tema agora é controlado aqui no topo para mudar a página INTEIRA
  const [theme, setTheme] = useState('dark');

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
  };

  return (
    <div className={`app ${theme}-theme`}>
      {/* Botão Flutuante de Alternar Tema posicionado no topo */}
      <button className="btn-theme-toggle" onClick={toggleTheme}>
        {theme === 'dark' ? '☀️ Modo Claro' : '🌙 Modo Escuro'}
      </button>

      <Header />
      
      <main className="conteudo-principal">
        {/* Passamos o tema atual para dentro do portfólio caso precise */}
        <Portfolio />
      </main>
      
      <Footer />
    </div>
  )
}

export default App