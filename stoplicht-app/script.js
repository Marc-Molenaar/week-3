async function start() {

    $(".light").css("background-color", "green")
    $("html").css("background-color", "red")
    $(".light").css("margin-left", "20px")
    await sleep(5);

    $(".light").css("background-color", "red")
    $("html").css("background-color", "yellow")
    $(".light").css("margin-left", "80px")
    await sleep(5);

    $(".light").css("background-color", "yellow")
    $("html").css("background-color", "green")
    $(".light").css("margin-left", "0px")
    await sleep(5);

    start()
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(document).ready(function() {
    start()
});