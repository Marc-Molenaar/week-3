async function start() {

    $(".light").css("background-color", "green")
    await sleep(20);
    $(".light").css("background-color", "red")
    await sleep(20);
    $(".light").css("background-color", "yellow")
    await sleep(20);
    $(".light").css("background-color", "white")
    await sleep(20);
    $(".light").css("background-color", "black")
    await sleep(20);
    $(".light").css("background-color", "indigo")
    await sleep(20);
    $(".light").css("background-color", "purple")
    await sleep(20);
    $(".light").css("background-color", "pink")
    await sleep(20);
    $(".light").css("background-color", "gray")
    await sleep(20);

    start()
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}