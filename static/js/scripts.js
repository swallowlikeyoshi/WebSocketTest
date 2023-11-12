$(document).ready(function(){
    var socket = io.connect('http://localhost:3000');
    socket.on('connect', function(){
        var connect_string = 'new_connect';
        socket.send(connect_string);
    });
    
    socket.on('hello', function(msg){
        $('#messages').append('<li>' + '>>Hello :' + msg + '</li>');
        console.log('Received Hello msg');
    });

    socket.on('message', function(msg){
        if (msg.type === 'normal') {
            $('#messages').append('>> ' + msg.message + '<br>');
        }
        else {
            $('#messages').append('<li>' + msg.message + '</li>');
        }

        console.log('Received "' + msg.type + '".')
    });

    $('#sendbutton').on('click', function(){
        socket.send($('#myMessage').val());
        $('#myMessage').val('');
    });
});