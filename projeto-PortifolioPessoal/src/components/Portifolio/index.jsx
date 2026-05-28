import React, { useState } from 'react';
import './style.css';

export default function Portfolio() {
  // Estado para controlar o tema (escuro por padrão)
  const [theme, setTheme] = useState('dark');

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
  };

  const habilidades = [
    { nome: "Lógica de Programação", status: "básico" },
    { nome: "Git & GitHub", status: "básico" },
    { nome: "Python", status: "básico" },
    { nome: "React.js", status: "em aprendizado" },
    { nome: "HTML & CSS", status: "em aprendizado" },
    { nome: "Bancos de Dados MySQL", status: "em aprendizado" },
  ];

  const listaProjetos = [
    {
      projeto: 1,
      titulo: "Anime Page",
      categoria: "JavaScript, HTML, CSS",
      descricao: "Páginas de indicações de anime, com papéis de parede duplos.",
      imagem: "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=500&auto=format&fit=crop&q=60",
      link: "https://github.com/jvictor7070/PA-99159-ATIVIDADE-01"
    },
    {
      projeto: 2,
      titulo: "Sistema de Cadastro (Em breve)",
      categoria: "Python, MySQL",
      descricao: "Projeto focado em persistência de dados e manipulação de banco de dados SQL.",
      imagem: "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=500&auto=format&fit=crop&q=60",
      link: "#"
    },
    {
      projeto: 3,
      titulo: "Estrutura de Dados (Em breve)",
      categoria: "Python",
      descricao: "Desafios de lógica e algoritmos desenvolvidos nas aulas do SENAI.",
      imagem: "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=500&auto=format&fit=crop&q=60",
      link: "#"
    }
  ];

  return (
    // Injeta dinamicamente a classe correspondente ao tema escolhido
    <div className={`portfolio-container ${theme}-theme`}>
      
      {/* Botão Flutuante de Alternar Tema */}
      <button className="btn-theme-toggle" onClick={toggleTheme}>
        {theme === 'dark' ? '☀️ Modo Claro' : '🌙 Modo Escuro'}
      </button>

      {/* BLOCO SUPERIOR: FOTO + NOME COMPLETO (Conforme o Rabisco) */}
      <header className="perfil-topo-row">
        <div className="foto-container">
          <img 
            src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&auto=format&fit=crop&q=80" 
            alt="João Victor dos Santos Coutinho" 
            className="foto-perfil"
          />
        </div>
        <div className="nome-container">
          <h1>João Victor dos Santos Coutinho</h1>
          <p className="subtitulo-cargo">Estudante ADS - SENAI</p>
        </div>
      </header>

      {/* BLOCO DO MEIO SUPERIOR: CONTATOS (Esquerda) e CONHECIMENTOS (Direita) */}
      <div className="info-intermediaria-row">
        
        {/* Contatos Empilhados à Esquerda */}
        <div className="contatos-coluna">
          <a 
            href="https://linkedin.com/in/joão-victor-dos-santos-coutinho-775405379" 
            target="_blank" 
            rel="noreferrer" 
            className="btn-rede btn-linkedin"
          >
            💼 LinkedIn
          </a>

          <a 
            href="mailto:joao.v.coutinho7@ba.estudante.senai.br" 
            className="btn-rede btn-email"
          >
            ✉️ E-mail
          </a>

          <a 
            href="https://wa.me/5571992643044" 
            target="_blank" 
            rel="noreferrer" 
            className="btn-rede btn-whatsapp"
          >
            📱 +55 71 99264-3044
          </a>
        </div>

        {/* Meus Conhecimentos à Direita */}
        <div className="conhecimentos-bloco">
          <h2>Meus Conhecimentos</h2>
          <div className="skills-grid">
            {habilidades.map((skill, index) => (
              <div key={index} className={`skill-tag ${skill.status.replace(" ", "-")}`}>
                <span>{skill.nome}</span>
                <small>{skill.status}</small>
              </div>
            ))}
          </div>
        </div>

      </div>

      {/* DIVISOR CENTRAL: PORTFÓLIO PROFISSIONAL */}
      <div className="divisor-central">
        <h2>Portfólio Profissional</h2>
      </div>

      {/* APRESENTAÇÃO SOBRE MIM */}
      <section className="secao-sobre-mim">
        <p>
          Olá! Sou estudante do 2º semestre de Análise e Desenvolvimento de Sistemas no <strong>SENAI - Bahia</strong>. 
          Estou focado em aprender a base sólida da programação e boas práticas de desenvolvimento. 
          Busco minha primeira oportunidade de estágio para aplicar na prática tudo o que desenvolvo em laboratório.
        </p>
      </section>

      {/* LISTA DE PROJETOS LADO A LADO */}
      <section className="secao-projetos">
        <div className="grid-projetos">
          {listaProjetos.map((proj) => (
            <div key={proj.projeto} className="card-projeto">
              
              <div className="card-imagem">
                <img src={proj.imagem} alt={proj.titulo} />
              </div>

              <div className="card-conteudo">
                <span className="categoria-tag">{proj.categoria}</span>
                <h3>{proj.titulo}</h3>
                <p>{proj.descricao}</p>
                {proj.link !== "#" ? (
                  <a href={proj.link} target="_blank" rel="noreferrer" className="link-projeto">
                    Ver no GitHub →
                  </a>
                ) : (
                  <span className="link-breve">Desenvolvendo...</span>
                )}
              </div>

            </div>
          ))}
        </div>
      </section>

    </div>
  );
}