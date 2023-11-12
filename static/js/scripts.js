$(document).ready(function(){

    var socket = io.connect('http://127.0.0.1');

    socket.on('connect', function(){
        var onConnect = "freshman"
        socket.send(onConnect);
    });

    const userName = prompt("사용자 이름 입력");
    console.log("username", userName);

    socket.on('login', userName, (responseFromServer)=>{
        console.log("Res?: ", responseFromServer);
    });

    socket.on('message', function(msg){
        if (msg.type === 'text') {
            $('#messages').append('>> ' + msg.message + '<br>');
        }
        else {
            $('#messages').append('<li>' + msg.message + '</li>');
        }

        console.log('Received "' + msg.type + '".')
    });

    $('#send').on('click', function(){
        socket.send($('#userInput').val());
        $('#userInput').val(''); // input 창 초기화
    });
    
});