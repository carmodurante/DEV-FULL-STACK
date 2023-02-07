function ordenar() {
    const lista = document.getElementById("valores");
    const tipoOrdenacao = document.getElementById("tipoOrdenacao");
    const itens = Array.from(lista.children);
    const valores = itens.map(item => parseInt(item.innerHTML));
    let algoritmoOrdenacao;
    switch (tipoOrdenacao.selectedIndex) {
        case 0:
            algoritmoOrdenacao = bubbleSort;
            break;
        case 1:
            algoritmoOrdenacao = selectionSort;
            break;
        case 2:
            algoritmoOrdenacao = quickSort;
            break;
        default:
            algoritmoOrdenacao = bubbleSort;
    }
    algoritmoOrdenacao(valores);
    lista.innerHTML = valores
        .map(valor => `<li>${valor}</li>`)
        .reduce((acumulador, item) => acumulador + item, "");
}
