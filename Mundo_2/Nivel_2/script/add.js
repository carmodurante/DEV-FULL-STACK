function add() {
    const input = document.getElementById("valor");
    const lista = document.getElementById("valores");
    const node = document.createElement("li");
    const textNode = document.createTextNode(input.value);
    node.appendChild(textNode);
    lista.appendChild(node);

}
