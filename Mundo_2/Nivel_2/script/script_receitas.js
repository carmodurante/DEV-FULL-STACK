var receitas = [
    {
        "titulo": "Arroz de Couve-Flor",
        "imagem": "content/arroz_de_couve_flor.jpg",
        "preparo": "Deixe o couve-flor picada. Adicione os ingredientes e reforgue bem. Adicione sal, tampe a panela e deixe cozinhar",
        "ingredientes": ['Arroz ',
            'Couve-Flor ',
            'Cebola Média ',
            'Azeite ']
    },
    {
        "titulo": "Bolo de Café",
        "imagem": "content/bolo_de_cafe.jpg",
        "preparo": "Bata o açúcar, as gemas e o café. Adicione farinha e chocolate e mexa bem. Bata as claras e junte à mistura.",
        "ingredientes": ['Farinha de Trigo',
            'Açúcar',
            'Café Coado',
            'Chocolate em Pó',
            'Ovos']
    },
    {
        "titulo": "Coxinha de Brigadeiro",
        "imagem": "content/coxinha_brigadeiro.jpg",
        "preparo": "Instruções de preparo da receita ",
        "ingredientes": ['Leite Condensado',
            'Chocolate em Pó',
            'Manteiga',
            'Morango',
            'Chocolate Granulado']
    }

];

function getListaIngredientes(receita) {
    var lista = "<ul>";
    for (var i = 0; i < receita.ingredientes.length; i++) {
        lista += "<li>" + receita.ingredientes[i] + "</li>";
    }
    lista += "</ul>";
    return lista;
}

function getCard(receita) {
    var card = "<div class='card'>";
    card += "<img src='" + receita.imagem + "' class='card-img-top'>";
    card += "<div class='card-body'>";
    card += "<h5 class='card-title'>" + receita.titulo + "</h5>";
    card += "<p class='card-text'>" + receita.preparo + "</p>";
    card += getListaIngredientes(receita);
    card += "</div>";
    card += "</div>";
    return card;
}

function preencheCatalogo() {
    for (var i = 0; i < receitas.length; i++) {
        document.getElementById("pnlCatalogo").innerHTML += getCard(receitas[i]);
    }
}

window.onload = preencheCatalogo;