function get_winners(channel, word, num_of_winners) {
    let url = 'https://7mq522bg73.execute-api.eu-north-1.amazonaws.com/Production/get_winners_of_guessor';
    let body = {
        'channel': channel,
        'word': word,
        'num_of_winners': num_of_winners
    }
    let response = fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
    .then( data => {
        return data.json();
    })
    .then( data => {
        let body = data.body;
        if (typeof body.winners !== "undefined") {
            console.log(body.winners);
            document.getElementById('spinner').style.display = "none";;
            let form = document.getElementById('winners');
            for (let i = 0; i < body.winners.length; i++) {
                form.innerHTML +=   '<div class="alert alert-primary mt-2" role="alert">'
                                    + (+i + +1) + ' место: ' + body.winners[i]
                                    + '</div>';
            }
            return body.winners;
        } else {
          return null;
        }
    })
    .catch(error => alert('Ошибка: таймаут 30 сек или др.'));
}

function changeInputFromRange() {
    let rangeInput = document.getElementById('num_of_winners');
    let input = document.getElementById('num_of_winners_input');
    input.value=rangeInput.value;
}

function changeRangeFromInput() {
    let rangeInput = document.getElementById('num_of_winners');
    let input = document.getElementById('num_of_winners_input');
    rangeInput.value=input.value;
}

function changeText() {
    let button = document.getElementById("collapse-button");
    let collapse = document.getElementById("word-collapse");
    if (button.value == "Скрыть слово" && collapse.className == "collapse show") {
        button.value = "Показать слово";
    }
    if (button.value == "Показать слово" && collapse.className == "collapse") {
        button.value = "Скрыть слово";
    }
    
}


let form = document.querySelector('.guesser');
form.addEventListener('submit', (e) => {
    let channel = form.elements['channel'].value;
    let word = form.elements['word'].value;
    let num_of_winners = parseInt(form.elements['num_of_winners_input'].value);
    let winners = get_winners(channel, word, num_of_winners);
    document.getElementById('spinner').style.display = "block";
});
