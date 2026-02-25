document.addEventListener("DOMContentLoaded", () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    socket.on('connect',() => {
        document.querySelector('button').forEach(b => {
            b.onclick = () => {
                const selection = b.dataset.vote;
                socket.emit('submit vote', {"selection":  selection});
            };
        });
    });

    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector("#votes").append(li);
    })
})