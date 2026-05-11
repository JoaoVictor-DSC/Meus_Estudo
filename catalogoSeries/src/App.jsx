import './App.css'
// O Vite entende automaticamente que deve buscar o index.jsx dentro das pastas
import Header from './components/Header' 
import AdicionarUsuario from './components/AdicionarUsuario'
import Footer from './components/Footer'

function App() {
  return (
    <div className='app'>
      <Header />
      <main>
        <AdicionarUsuario />
      </main>
      <Footer/>
    </div>
  )
}

export default App