const form = document.getElementById('formulario')

form.addEventListener('submit', (e) => {
    e.preventDefault(); //evitar recarregamento de página
    let nome = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let data = {
        nome,
        email,
    }

    let convertData = JSON.stringify(data);

    localStorage.setItem('lead', convertData)

    let content = document.getElementById('conteudo')
    let carregando = `<p>carregando ...</p>`
    let pronto = `<p>Pronto!</p>`

    content.innerHTML = carregando
    setTimeout(() => {
        content.innerHTML = pronto
    }, 1000)
    // console.log(nome, email);
    
    // alert('Cadastro concluído!');
})