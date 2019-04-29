function first(){
    var chat = document.getElementsByClassName('conversation-view')[0];

    var chatAi = document.createElement('div');

    var chatSpan = document.createElement('span');

    chatAi.setAttribute('class', 'chat-bubble');
    chatSpan.setAttribute('class', 'chat-content');

    var chatText = document.createTextNode('어떤 영화를 찾으시나요? 여러 영화를 찾아드립니다.');

    chatSpan.appendChild(chatText);
    chatAi.appendChild(chatSpan);
    chat.appendChild(chatAi);


    chatAi = document.createElement('div');

    chatSpan = document.createElement('span');

    chatAi.setAttribute('class', 'chat-bubble');
    chatSpan.setAttribute('class', 'chat-content');

    chatText = document.createTextNode('최근 영화 / 인기 영화 / 장르별 추천 영화 / 연도별 추천 영화 / 영화 검색 / 오늘의 영화');

    chatSpan.appendChild(chatText);
    chatAi.appendChild(chatSpan);
    chat.appendChild(chatAi);
}