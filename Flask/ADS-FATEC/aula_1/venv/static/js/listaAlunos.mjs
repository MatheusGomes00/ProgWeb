// Obtém os dados armazenados no localStorage e os converte para um vetor de alunos
var dados = localStorage.getItem('dados')
var alunos = dados ? JSON.parse(dados) : []

// referencia do form
var tabela = document.getElementById('Alunos')

// Limpa o conteúdo da tabela.
tabela.innerHTML = ""

// Obtem a URL atual da pagina.
const currentURL = window.location.href

// Analisa os parâmetros da URL usando o objeto URL.
const url = new URL(currentURL)

// Obtem os parâmetros "ordem" e "apenas" da URL, que são usados para ordenar e filtrar os alunos
const searchParams = url.searchParams
const ordem = searchParams.get("ordem")
const resultado = searchParams.get("apenas")



// Função de ordenação Bubble Sort.
function bubbleSort(vetor, fnComp) {
    let swap
    do {
        swap = false;
        for (let i = 0; i < vetor.length - 1; i++) {
            if (fnComp(vetor[i], vetor[i + 1])) {
                // Troca os elementos no vetor se necessário.
                [vetor[i], vetor[i + 1]] = [vetor[i + 1], vetor[i]]
                swap = true
            }
        }
    } while (swap)
}

// Filtra os alunos com base no resultado (Aprovado ou não)
alunos = alunos.filter(aluno => {
    if (resultado) {
        return aluno.resultado == 'Aprovado'
    } else {
        return true
    }
})

// Ordena os alunos com base no nome usando o Bubble Sort em ordem crescente pelo nome.
bubbleSort(alunos, (a, b) => {
    var nameA = a.nome.toLowerCase()
    var nameB = b.nome.toLowerCase()
        return nameA > nameB
})

bubbleSort(alunos, (a, b) => {
    var raA = a.ra
    var raB = b.ra
    if(ordem === 'decrescente'){
        return raA < raB
    }
})

if(ordem === 'decrescente'){
    document.getElementById('inTitulorelatorio').innerHTML = 'Relatório de Alunos em ordem decrescente por RA'
}else if(resultado === 'aprovados'){
    document.getElementById('inTitulorelatorio').innerHTML = 'Relatório de Alunos em ordem crescente por Nome, apenas dos Aprovados'
}else{
    document.getElementById('inTitulorelatorio').innerHTML = 'Relatório de Alunos em ordem crescente por Nome'
}


// cria a tabela
alunos.forEach(aluno => {
    var linha = document.createElement("tr")

    // Cria células para cada atributo do aluno e preenche com os dados.
    var nome = document.createElement("td")
    nome.textContent = aluno.nome

    var ra = document.createElement("td")
    ra.textContent = aluno.ra

    var idade = document.createElement("td")
    idade.textContent = aluno.idade

    var sexo = document.createElement("td")
    sexo.textContent = aluno.sexo

    var media = document.createElement("td")
    media.textContent = aluno.media

    var resultado = document.createElement("td")
    resultado.textContent = aluno.resultado

    // Adiciona as informações na tabela
    linha.appendChild(nome)
    linha.appendChild(ra)
    linha.appendChild(idade)
    linha.appendChild(sexo)
    linha.appendChild(media)
    linha.appendChild(resultado)
    tabela.appendChild(linha)
})

// função voltar a index
document.addEventListener('DOMContentLoaded', function (){
    const btVoltar = document.getElementById('inVoltar')

    if(btVoltar){
        btVoltar.addEventListener('click', function (){
            window.location.href = "/menu"
        })
    }
});



