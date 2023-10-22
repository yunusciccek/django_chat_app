// static/js/js.py
const user = JSON.parse(document.getElementById('user').textContent);

const conversation = document.getElementById('conversation');




window.addEventListener("DOMContentLoaded", function () {
    // Oda adını al
    const roomName = document.getElementById('room-name').textContent;

    // WebSocket bağlantısını başlat
    const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        // Mesajları işleyin ve görüntüleyin
        const chatLog = document.getElementById('chat-log');
        chatLog.value += data.message + '\n';
        
        
        if (user == data.user) {
            var message = `
            <div class="row message-body">
                <div class="col-sm-12 message-main-sender">
                    <div class="sender">
                        <div class="message-text">
                            ${data.message}
                        </div>
                        <span class="message-time pull-right">
                            ${data.created_date}
                        </span>
                    </div>
                </div>
            </div>
        `;
        }else{
            var message = `
        <div class="row message-body">
            <div class="col-sm-12 message-main-receiver">
                <div class="receiver">
                    <div class="message-text">
                        ${data.message}
                    </div>
                    <span class="message-time pull-right">
                        ${data.created_date}
                    </span>
                </div>
            </div>
        </div>
    `;
            



        }





        conversation.innerHTML += message;


        
        
    };
    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    // Mesaj gönderme
    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function (e) {
        if (e.keyCode === 13) {  // enter, return
            if (document.querySelector('#chat-message-submit')) {
                document.querySelector('#chat-message-submit').click();
            }
        }
    };

    document.querySelector('#chat-message-submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.value = '';
    };
}
);



