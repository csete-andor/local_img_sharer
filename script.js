document.addEventListener("DOMContentLoaded", function() {
    var qrcode = new QRCode(document.getElementById("qrcode"), {
        text: window.location.href,
        width: 128,
        height: 128,
    });
});
