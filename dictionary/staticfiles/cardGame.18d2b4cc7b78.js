console.log('ok');
const sections = document.querySelector('section')
const cards = document.querySelectorAll('.card')


for(element of cards) {
        element.addEventListener('click', function (e) {
            e.currentTarget.classList.toggle('toggleCard');
        })
    }


// const createCard = function(){
//     for( card of cards) {
//         const card = document.createElement('div');
//         const word = document.createElement('div');
//         const definition = document.createElement('div');
//         card.classList.add('card');
//         word.classList.add('word');
//         word.innerText = "word"
//         definition.classList.add('definition');
//         definition.innerText = 'definition and somthing else'
//         sections.appendChild(card);
//         card.appendChild(word);
//         card.appendChild(definition);
//         card.addEventListener('click', function (e) {
//             card.classList.toggle('toggleCard');
//         })
//     }
// }
//
// createCard()