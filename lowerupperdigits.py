from cgitb import html


<html>
<script>
let message=msg.value
let i=0
function copyUpper(){
while(i<message.length){
    if (message.charCodeAt(i)>=65 && message.charCodeAt(i)<=90){
        newmsg.value+=message.substring(i,i+1)
    }
    i=++
}
}
function copylower(){
while(i<message.length){
    if (message.charCodeAt(i)>=97 && message.charCodeAt(i)<=122){
        newmsg.value+=message.substring(i,i+1)
    }
    i=++
}
}
function copydigits(){
while(i<message.length){
    if (message.charCodeAt(i)>=48 && message.charCodeAt(i)<=57){
        newmsg.value+=message.substring(i,i+1)
    }
    i=++
}
}
</script>
Enter Message :<input type="text" id="msg" <br>
<input type="button" value="copy UpperCaseLetters" onclick="copyUpper()">
<input type="button" value="copy LowercaseLetters" onclick="coppylower()"
<input type="button" value="copy Copy Digits" onclick="copydigits()"

<br>
New message:<input type="text" id="newmsg"> <br>
