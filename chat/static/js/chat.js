/**
 * Created by tadej on 29.04.15.
 */



//setInterval(
function update() {
    var id = $('.message:last').attr('id');
    alert("text: " + id);

    var answer = $.ajax({
        type: "POST",
        url: 'update_message',
        data: "id=" + id
    }).responseText;
    alert("answer: " + answer);
}
//, 1000)


function send_message() {
    var user = document.getElementById('user').value;
    var text = document.getElementById('text').value;
    alert("text: " + text + ", user: " + user + ".");

    xhttp = new XMLHttpRequest();
    xhttp.open('POST', 'send_message', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var message = 'user=' + user + '&text=' + text;
    xhttp.send(message);
}


