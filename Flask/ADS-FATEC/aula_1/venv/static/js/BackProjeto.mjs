// navegação pelo menu
document.addEventListener('DOMContentLoaded', function () {
    const btExecutar = document.getElementById('inExecutar')

    if(btExecutar){
        btExecutar.addEventListener('click', function () {
            const opcao = document.getElementById("inTextexecucao").value 
            
            switch (opcao){
                case '1':
                    window.location.href = "/cadastro"
                    break
                case '2':
                    window.location.href = "/listar"
                    break
                case '3':
                    window.location.href = "listar?ordem=decrescente"
                    break
                case '4':
                    window.location.href = "/listar?apenas=aprovados"
                    break
                case '5':
                    localStorage.clear()
                    window.location.href = "/"
                    break              
                default:
                    alert("Número Inválido")
                    break
            }
        })
    }
})

// abre o menu do projeto
document.addEventListener('DOMContentLoaded', function (){
    const btIniciar = document.getElementById('inInicio')
    if(btIniciar){
        btIniciar.addEventListener('click', function (){
            window.location.href = "/menu"
        })
    }
})

// opção de voltar da página de cadastro   
document.addEventListener('DOMContentLoaded', function (){
    const btVoltar = document.getElementById('inVoltar')

    if(btVoltar){
        btVoltar.addEventListener('click', function (){
            window.location.href = "/menu"
        })
    }
})


document.addEventListener('DOMContentLoaded', function (){
    const btListaTeste = document.getElementById('inListaTeste')
    if(btListaTeste){
        btListaTeste.addEventListener('click', function (){
            alert("Cadastrado 10 alunos para teste.")
            localStorage.clear()
            alunos = [
                { 'nome': 'Alice', 'ra': 12345, 'idade': 25, 'sexo': 'Feminino', 'media': 7, 'resultado': 'Aprovado' },
                { 'nome': 'Bob', 'ra': 67890, 'idade': 22, 'sexo': 'Masculino', 'media': 5, 'resultado': 'Reprovado' },
                { 'nome': 'Carol', 'ra': 54321, 'idade': 20, 'sexo': 'Feminino', 'media': 8, 'resultado': 'Aprovado' },
                { 'nome': 'David', 'ra': 98765, 'idade': 27, 'sexo': 'Masculino', 'media': 6, 'resultado': 'Reprovado' },
                { 'nome': 'Eve', 'ra': 13579, 'idade': 24, 'sexo': 'Feminino', 'media': 9, 'resultado': 'Aprovado' },
                { 'nome': 'Frank', 'ra': 24680, 'idade': 28, 'sexo': 'Masculino', 'media': 4, 'resultado': 'Reprovado' },
                { 'nome': 'Grace', 'ra': 11223, 'idade': 21, 'sexo': 'Feminino', 'media': 7, 'resultado': 'Aprovado' },
                { 'nome': 'Helen', 'ra': 33445, 'idade': 29, 'sexo': 'Feminino', 'media': 8, 'resultado': 'Aprovado' },
                { 'nome': 'Ivy', 'ra': 55667, 'idade': 23, 'sexo': 'Feminino', 'media': 6, 'resultado': 'Reprovado' },
                { 'nome': 'Jack', 'ra': 77889, 'idade': 26, 'sexo': 'Masculino', 'media': 9, 'resultado': 'Aprovado' }
            ]
            localStorage.setItem('dados', JSON.stringify(alunos))
        })
    }
    else{
        
    }

})


//criar array dos dados
var form = document.getElementById("formAluno");
var dados = localStorage.getItem('dados')
var alunos = dados ? JSON.parse(dados) : []



form?.addEventListener("submit", function(event) {
    event.preventDefault();

    var nome = document.getElementById("inNome").value;
    var ra = document.getElementById("inRa").value;
    var idade = document.getElementById("inIdade").value;
    var sexo = document.getElementById("inSexo").value
    var media = document.getElementById("inMedia").value
    var resultado = document.getElementById("inResultado").value

    alunos.push({
        nome,
        ra,
        idade,
        sexo,
        media,
        resultado
      })
    
    localStorage.setItem('dados', JSON.stringify(alunos))
    var nome = document.getElementById("inNome").value = ''
    var ra = document.getElementById("inRa").value = ''
    var idade = document.getElementById("inIdade").value = ''
    var sexo = document.getElementById("inSexo").value = ''
    var media = document.getElementById("inMedia").value = ''
    var resultado = document.getElementById("inResultado").value = ''
});




