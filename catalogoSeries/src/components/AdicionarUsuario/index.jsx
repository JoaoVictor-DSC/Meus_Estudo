import './style.css'
import { useState } from 'react'

export default function AdicionarUsuario() {
    const[usuario, setUsuario] = useState('')
    const[stand, setStand] = useState('')
    const[habilidades, setHabilidades] = useState('')
    const[listaUsuarios, setListaUsuarios] = useState([])

    const handlerSubmit = (e) => {
        e.preventDefault() // Corrigido de 'event' para 'e'
        if(usuario && stand && habilidades){   
            setListaUsuarios([...listaUsuarios, {usuario, stand, habilidades}])
            setUsuario('')
            setStand('')
            setHabilidades('')
        }
    }

    // O return deve ficar fora do handlerSubmit!
    return(
        <div className='formulario-jojo'>
            <h2>Catálogo de Stands</h2>
            <form onSubmit={handlerSubmit}>
                <input
                    type="text"
                    value={usuario}
                    placeholder='Mestre (Usuário)'
                    onChange={(e) => setUsuario(e.target.value)}
                />
                <input 
                    type="text"
                    value={stand}
                    placeholder='Nome do Stand'
                    onChange={(e)=> setStand(e.target.value)} 
                />
                <input 
                    type="text"
                    value={habilidades}
                    placeholder='Habilidades (ex: Parar o tempo)'
                    onChange={(e)=> setHabilidades(e.target.value)} 
                />
                <button type="submit">Invocar Stand!</button>
            </form>

            <hr className='linha-divisoria'/>
            
            <h2>Lista de Usuários</h2>
            <ul>
                {listaUsuarios.map((item, index) => (
                    <li key={index} className='stand-card'>
                        <strong>Usuário:</strong> {item.usuario} <br />
                        <strong>Stand:</strong> <span className='stand-name'>{item.stand}</span> <br />
                        <strong>Habilidades:</strong> {item.habilidades}
                    </li>
                ))}
            </ul>
        </div>
    )    
}