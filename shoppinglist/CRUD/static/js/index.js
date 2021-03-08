var divPrincipal = document.getElementById("divPrincipal")

function adicionaProduto() {
    var bloco = document.createElement('div')
    bloco.style.backgroundColor = 'yellow'
    bloco.style.height = '200px'
    bloco.style.width = '200px'
    bloco.style.margin = "30px 35px 30px 40px"
    bloco.style.borderRadius = '20px'

    var nomeProduto = document.getElementById('idProduto').value
    var quantidade = document.getElementById('idQuantidade').value
    
    var txtProduto = document.createElement('p')
    txtProduto.innerText = nomeProduto
    txtProduto.style.fontSize = '14pt'
    txtProduto.style.padding = '0'

    var txtQuantidade = document.createElement('p')
    txtQuantidade.innerText = quantidade
    txtQuantidade.style.fontSize = '14pt'

    var labelProduto = document.createElement('p')
    labelProduto.innerHTML = "<strong>Produto:</strong> <br>"
    labelProduto.style.fontSize = '14pt'
    labelProduto.style.paddingTop = '10px'
    labelProduto.style.paddingLeft = "15px"

    var labelQuantidade = document.createElement('p')
    labelQuantidade.innerHTML = "<strong>Quantidade:</strong> <br>"
    labelQuantidade.style.fontSize = '14pt'
    labelQuantidade.style.paddingTop = '1px'
    labelQuantidade.style.paddingLeft = "15px"

    bloco.appendChild(labelProduto)
    bloco.appendChild(txtProduto)
    bloco.appendChild(labelQuantidade)
    bloco.appendChild(txtQuantidade)


    divPrincipal.appendChild(bloco)
}