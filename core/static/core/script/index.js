var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/game');

var commands = {
	'error': error,
	'ping': ping,
	'message': message,
	'take_sprite': take_sprite,
	'move_sprite': move_sprite,
	'release_sprite': release_sprite,
	'update_map': update_map
};

chatSocket.onmessage = function(e) {
    console.log('received');
    var data = JSON.parse(e.data);
    var command = data['command'];

	try {
		commands[command](data);
    } catch(e) {
		console.error('Server sent an unknown command: ');
		console.error(data)
	}
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

//===== HANDLERS =====
function error(data) {
    console.error(data.message);
}

function ping(data) {
	var x = data['position-x'];
	var y = data['position-y'];
	var color = data['color'];
	console.log('ping: ' + x + ';' + y + ' ' + color)
}

function message(data) {
	var message = data['message'];
}

function take_sprite(data) {
	var sprite_id = data['sprite_id'];
	var color = data['color'];
}

function move_sprite(data) {
	var sprite_id = data['sprite_id'];
	var x = data['position-x'];
	var y = data['position-y'];
}

function release_sprite(data) {
	var sprite_id = data['sprite_id'];
}

function update_map(data) {
	var map_id = data['map_id'];
}

//===== PAGE DYNAMIC =====

early_selections = document.querySelectorAll('#early_selections .selectable');
Array.from(early_selections).forEach(selection => {
    selection.addEventListener('click', function(e) {
		document.getElementById('early_selections').classList.add('hidden');
	});
});

tab_grabs = document.querySelectorAll('.tab_grab');
Array.from(tab_grabs).forEach(grab => {
	grab.addEventListener('click', function(e) {
		if(e.target.classList.contains('active')) {
			e.target.parentElement.parentElement.classList.remove('panel_out'); /* retract panel */
			e.target.classList.remove('active'); /* desactivate current grab */
			var tab_id = e.target.getAttribute('tab'); /* find linked tab's id */
			document.getElementById(tab_id).classList.remove('active') /* desactivate current tab */
		} else {
			e.target.parentElement.parentElement.classList.add('panel_out'); /* extract panel if not already done */
			var prev = e.target.parentElement.querySelector('.active') /* find last active grab */
			if(prev) {
				prev.classList.remove('active');
				prev_tab_id = prev.getAttribute('tab'); /* find previous linked tab's id */
				document.getElementById(prev_tab_id).classList.remove('active'); /* desactivate previous tab */
			}
			e.target.classList.add('active'); /* activate current grab */
			var tab_id = e.target.getAttribute('tab'); /* find linked tab's id */
			document.getElementById(tab_id).classList.add('active') /* activate tab */
		}
	});
});

characters = document.querySelectorAll('.character');
Array.from(characters).forEach(character => {
    character.addEventListener('click', function(e) {
		e.target.classList.toggle('selected');
	});
});

function update(url, id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true); // false for synchronous request

	xmlHttp.onreadystatechange = function() {
    	document.getElementById(id).innerHTML = xmlHttp.responseText;
	};
    xmlHttp.send(null);
}

/*document.querySelector('.player').onclick = function(e) {
	update("player_selection", "player_selection_content");	
};
*/


/*
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'command': 'message',
        'message': message
    }));
    chatSocket.send(JSON.stringify({
        'command': 'ping',
        'position-x': 0, 
        'position-y': 0
    }));

    messageInputDom.value = '';
};
*/
