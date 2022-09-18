function copy_to_clipboard() {
    var copyText = document.getElementById("result");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
}
function validate() {
    var reg = /<(.|\n)*>/g;
    if (reg.test(document.getElementById("data").value) == true) {
        var ErrorText = 'Please enter text in correct format';
        alert(ErrorText);
        return;
    }
}
