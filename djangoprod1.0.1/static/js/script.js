console.log("js its runn");
alert("hello in js web browser");
console.warn('This is warning');
function changeText(){
    const parameter = document.getElementById("message");
    parameter.innerText = "voce clicou aqui nesse botao";
}

function gmailConfirm(){
    const paragraph = document.getElementById("myParagraphTest");
    if (paragraph){
        paragraph.textContent = "gmailConfirm Test in js";
        paragraph.style = "black";
        paragraph.style = "bold";
    }



}