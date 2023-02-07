const swap = (arr, i, j) => [arr[i], arr[j]] = [arr[j], arr[i]];

const shuffle = (arr, n) => {
    for (let i = 0; i < n; i++) {
        let j = Math.floor(Math.random() * arr.length);
        swap(arr, i, j);
    }
    return arr;
};

const bubbleSort = arr => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
    }
    return arr;
};

const selectionSort = arr => {
    for (let i = 0; i < arr.length - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex !== i) {
            swap(arr, i, minIndex);
        }
    }
    return arr;
};

const quickSort = (arr, start, end) => {
    if (start < end) {
        let pivotIndex = particionamento(arr, start, end);
        quickSort(arr, start, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, end);
    }
    return arr;
};

const particionamento = (arr, start, end) => {
    let pivot = arr[end];
    let i = start - 1;
    for (let j = start; j <= end - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, end);
    return i + 1;
};

function add() {
    const input = document.getElementById("valor");
    const lista = document.getElementById("valores");
    const node = document.createElement("li");
    const textNode = document.createTextNode(input.value);
    node.appendChild(textNode);
    lista.appendChild(node);

}

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

function misturar() {
    const lista = document.getElementById("valores");
    const itens = Array.from(lista.children);
    const valores = itens.map(item => parseInt(item.innerHTML));
    shuffle(valores);
    lista.innerHTML = valores
        .map(valor => `<li>${valor}</li>`)
        .reduce((acumulador, item) => acumulador + item, "");
} 