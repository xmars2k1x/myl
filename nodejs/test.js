var http = require('http'),
	Io = require('socket.io'),
	redis = require('redis'),
	cookie = require('cookie'),
	serialize = require('node-serialize'),
	redisClient = redis.createClient(6379, '127.0.0.1');

var server = http.createServer(function (req, res) {
	//
});

server.listen(3000);

io = Io.listen(server);

io.on('connection', function (socket) {
	console.log('Client connected.');
	socket.on('disconnect', function () {
		console.log('Client disconnected.');
	});
	socket.on('chat message', function (msg) {
		io.emit('chat message', msg);
	});
});

/*io.use(function (socket, next) {
	auth(socket, next);
});*/

/*
io.sockets.on('connection', function (socket) {
	socket.emit('join', socket.handshake.user);
});
*/

function auth (socket, next) {
	var userCookie = cookie.parse(socket.request.headers.cookie);
	redisClient.get('session:' + userCookie.nodejskey, function (err, session) {
		if(err || !session){
			return next(new Error('Not authorized.'));
		}
		session = serialize.unserialize(session);
		socket.handshake.user = session.user;
		if(session.user == 'xmars2k1x'){
			next();
		}
		else {
			return next(new Error('Not authorized.'));
		}
	});
}