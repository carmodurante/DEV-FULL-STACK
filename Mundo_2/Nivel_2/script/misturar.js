function misturar() {
    const lista = document.getElementById("valores");
    const itens = Array.from(lista.children);
    const valores = itens.map(item => parseInt(item.innerHTML));
    shuffle(valores);
    lista.innerHTML = valores
        .map(valor => `<li>${valor}</li>`)
        .reduce((acumulador, item) => acumulador + item, "");
}
