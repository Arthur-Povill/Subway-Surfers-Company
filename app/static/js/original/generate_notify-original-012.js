const nomes = [
    "Alice", "Lucas", "Sofia", "Pedro", "Laura", "Miguel", "Isabella", "Gabriel", "Valentina", "Matheus",
    "Maria", "Arthur", "Helena", "Bernardo", "Luiza", "Davi", "Beatriz", "Heitor", "Giovanna", "Samuel",
    "Clara", "Enzo", "Maria Eduarda", "João", "Julia", "Henrique", "Lívia", "Lucca", "Mariana", "Gustavo",
    "Isadora", "Rafael", "Gabriela", "Felipe", "Lara", "Daniel", "Amanda", "Theo", "Natália", "Benjamin",
    "Sophia", "Murilo", "Camila", "Luiz", "Eloá", "Bruno", "Valéria", "Leo", "Yasmin", "Bryan", "Ayla", "Caio",
    "Sofia", "Lucas", "Alice", "Arthur", "Isabella", "Pedro", "Laura", "Gabriel", "Valentina", "Matheus",
    "Maria", "Miguel", "Helena", "Davi", "Giovanna", "Maria Eduarda", "Bernardo", "Luiza", "Heitor", "Clara",
    "Samuel", "Beatriz", "Enzo", "João", "Julia", "Gustavo", "Mariana", "Henrique", "Isadora", "Lucca", "Gabriela",
    "Clara", "Rodrigo", "Yasmin", "Felipe", "Amanda", "Carlos", "Renata", "Thiago", "Carol", "Matias", "Sofia",
    "Gustavo", "Marina", "Felipe", "Ana", "Caio", "Laura", 'Luan', 'Larissa', 'João', 'Lorena', 'Rafael', 'Lara',
    'Guilherme', 'Manuela', 'Nicolas', 'Júlia', 'Breno', 'Lívia', 'Eduardo', 'Beatriz', 'Vinícius', 'Isabelly',
    'João', 'Sarah', 'Luiz', 'Ana', 'Gustavo', 'Maria', 'Henrique', 'Ana', 'Daniel', 'Carolina', 'Pedro', 'Amanda',
    'Leonardo', 'Maria', 'Murilo', 'Isabela', 'Vitor', 'Lavínia', 'João', 'Gabrielly', 'Emanuel', 'Ana', 'João',
    'Mari', 'Luiz', 'Vitor',
];
  
const sobrenomes = [
    "Silva", "Santos", "Pereira", "Ferreira", "Oliveira", "Souza", "Rodrigues", "Almeida", "Lima", "Costa",
    "Castro", "Fernandes", "Ribeiro", "Carvalho", "Gomes", "Martins", "Araújo", "Barbosa", "Correia", "Fernandes",
    "Machado", "Pinto", "Moraes", "Cardoso", "Dias", "Marques", "Ferreira", "Moreira", "Nunes", "Barbosa",
    "Ribeiro", "Oliveira", "Castro", "Almeida", "Costa", "Santos", "Rodrigues", "Pereira", "Lima", "Souza",
    "Silva", "Gomes", "Carvalho", "Martins", "Correia", "Fernandes", "Araújo", "Machado", "Pinto", "Moraes",
    "Cardoso", "Dias", "Moreira", "Nunes", "Marques", "Ramos", "Cunha", "Fonseca", "Ferreira", "Barbosa",
    "Dias", "Pereira", "Lima", "Castro", "Ribeiro", "Souza", "Santos", "Oliveira", "Rodrigues", "Almeida",
    "Costa", "Carvalho", "Martins", "Machado", "Gomes", "Fernandes", "Correia", "Moraes", "Pinto", "Cardoso",
    "Moreira", "Nunes", "Araújo", "Marques", "Cunha", "Ferreira", "Barbosa", "Lima", "Dias", "Pereira", "Silva",
    "Ribeiro", "Castro", "Carvalho", "Souza", "Rodrigues", "Martins", "Gomes", "Oliveira", "Correia",
    "Almeida", "Machado", "Fernandes", "Costa", "Pinto", "Moreira", "Moraes", "Cardoso", "Araújo", "Nunes",
    "Marques", "Ferreira", "Barbosa", "Cunha", "Ramos", "Fonseca", "Silva", "Santos", "Pereira", "Ferreira",
];

function generateAleatoryName() {
const nomeAleatorio = nomes[Math.floor(Math.random() * nomes.length)];
const sobrenomeAleatorio = sobrenomes[Math.floor(Math.random() * sobrenomes.length)];
return nomeAleatorio + " " + sobrenomeAleatorio;
}

function formatCurrencyBrazilian(number) {
    try {
        number = parseFloat(number);
    } catch (e) {
    }
    let formattedNumber = number.toFixed(2).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, '$1.');

    return formattedNumber;
}

function notification(){
    let list_event = ['deposit', 'withdraw', 'gain'];
    let randomNumber = Math.random();
    let event_notify;
    if (randomNumber < 0.75) {
    event_notify = 'withdraw';
    } else {
    event_notify = (randomNumber < 0.875) ? 'deposit' : 'gain';
    }
    let random_name = generateAleatoryName();
    let container = document.querySelector('.notification-gain-container');
    if(container.childElementCount == 1){
        container.removeChild(container.firstElementChild);
    }
    let div = document.createElement('div');
    div.classList.add('notify-gain');
    let span = document.createElement('span');
    let html = '';
    if(event_notify == 'deposit'){
        var value = Math.floor(Math.random() * (100 - 20 + 1)) + 20;
        value = formatCurrencyBrazilian(value);
        html = '<span class="bolded">' + random_name + '</span> realizou um depósito de <span class="bolded">R$' + value + '<span>';
    }else if(event_notify == 'withdraw'){
        var value = Math.floor(Math.random() * (175 - 50 + 1)) + 50;
        value = formatCurrencyBrazilian(value);
        html = '<span class="bolded">' + random_name + '</span> realizou um saque de <span class="bolded">R$' + value + '<span>';
    }else{
        var value = Math.floor(Math.random() * (100 - 5 + 1)) + 5;
        value = formatCurrencyBrazilian(value);
        html = '<span class="bolded">' + random_name + '</span> ganhou <span class="bolded">R$' + value + '<span> no jogo do subway';
    }
    span.innerHTML = html;
    div.appendChild(span);
    container.appendChild(div);
    setTimeout(function () {
        container.removeChild(container.firstElementChild);
        setTimeout(function () {}, 5000);
    }, 5000);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function callNotification(){
    const minInterval = 4000;
    const maxInterval = 8000;
    const dynamicInterval = Math.floor(Math.random() * (maxInterval - minInterval + 1)) + minInterval;
    setInterval(notification, dynamicInterval);
}

callNotification();