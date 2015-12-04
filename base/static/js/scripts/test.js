define(['http://localhost:3000/socket.io/socket.io.js'], function (io) {
	var socket = io('http://localhost:3000');

	$('#enviar').click(function () {
		console.log('el boton enviar a sido presionado');
		socket.emit('chat message', $('#inputz').val());
		$('#inputz').val('');
	});

	socket.on('chat message', function (msg) {
		console.log(msg);
		$('#chat').append('<div class="text">' + msg + '</div>');
	});
});