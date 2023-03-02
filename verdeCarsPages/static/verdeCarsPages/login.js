import(verdeCarsPages/models.py);

function verifyUser() {
    alert("Poot Woot");
    for (userName in User.objects.all) {
        alert(userName);
    }
}
