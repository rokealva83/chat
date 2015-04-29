/**
 * Created by tadej on 29.04.15.
 */

function send_message() {
    var user = document.getElementById('user').value;
    var text = document.getElementById('text').value;
    alert("text: " + text + ", user: " + user + ".");

    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200)
            document.getElementById("ajax").innerHTML = xhttp.responseText;
    }
    xhttp.open('POST', 'send_message', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var message = 'user='+user+'&text='+text;
    xhttp.send(message);
}