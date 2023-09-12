async function start() {

    $(".light").css("background-color", "green")
    await sleep(5);
    $(".light").css("background-color", "red")
    await sleep(5);
    $(".light").css("background-color", "yellow")
    await sleep(5);

    start()
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}