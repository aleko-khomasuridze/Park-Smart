
// Function to open the "pay.html" page
function pay() {
    window.open("pay.html", "_self");
}

// Function to open the "main.html" page
function quit() {
    window.open("main.html", "_self");
}

// Function to simulate a purchase action
function buy() {
    // Open the "main.html" page
    window.open("main.html", "_self");
    
    // Change the style of an element with the id "p2" to indicate a purchase
    document.getElementById("p2").style.backgroundColor = "rgba(164, 83, 119, 0.4)";
    document.getElementById("p2").style.color = "rgba(228, 156, 182, 0.8)";
}

// Function to retrieve data from Python using Eel
async function run() {
    let n = await eel.sendData()();
    document.getElementById("p1").innerText = n;
    console.log('Got this from Python: ' + n);
}

// Run the "run" function to fetch and display data from Python
run();

// Function to prepare for payment using MasterCard
function getReadyToPayMC() {
    // Change styles of various elements to indicate MasterCard payment
    document.getElementById("p2").style.backgroundColor = "rgba(164, 83, 119, 0.4)";
    document.getElementById("p2").style.color = "rgba(228, 156, 182, 0.8)";
    document.getElementById("p2").style.borderBlockColor = "rgba(166, 70, 106, 1)";
    document.getElementById("mc").style.backgroundColor = "rgba(45, 50, 59, 1)";
    document.getElementById("VISA").style.backgroundColor = "rgba(34, 39, 46, 1)";
    document.getElementById("payC").style.backgroundColor = "rgba(74, 118, 137, 1)";
}

// Function to prepare for payment using VISA
function getReadyToPayVISA() {
    // Change styles of various elements to indicate VISA payment
    document.getElementById("VISA").style.backgroundColor = "rgba(45, 50, 59, 1)";
    document.getElementById("mc").style.backgroundColor = "rgba(34, 39, 46, 1)";
    document.getElementById("payC").style.backgroundColor = "rgba(74, 118, 137, 1)";
}

// Functions to select parking options
function selectPC1() {
    // Change styles to highlight the first parking option
    document.getElementById("pc1").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("pc1").style.color = "white";
    for (let i = 1; i <= 4; i++) {
        if (i == 1) {
            continue;
        }
        document.getElementById("pc" + String(i)).style.backgroundColor = "rgba(34, 39, 46, 0.6)";
        document.getElementById("pc" + String(i)).style.color = "rgba(96, 106, 119, 1)";
    }
    document.getElementById("book").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("book").style.color = "white";
    document.getElementById("book").innerText = "Book For: 5.99₾";
}

// Functions to select parking options
function selectPC2() {
    // Change styles to highlight the second parking option
    document.getElementById("pc2").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("pc2").style.color = "white";
    for (let i = 1; i <= 4; i++) {
        if (i == 2) {
            continue;
        }
        document.getElementById("pc" + String(i)).style.backgroundColor = "rgba(34, 39, 46, 0.6)";
        document.getElementById("pc" + String(i)).style.color = "rgba(96, 106, 119, 1)";
    }
    document.getElementById("book").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("book").style.color = "white";
    document.getElementById("book").innerText = "Book For: 5.99₾";
}

// Functions to select parking options
function selectPC3() {
    // Change styles to highlight the third parking option
    document.getElementById("pc3").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("pc3").style.color = "white";
    for (let i = 1; i <= 4; i++) {
        if (i == 3) {
            continue;
        }
        document.getElementById("pc" + String(i)).style.backgroundColor = "rgba(34, 39, 46, 0.6)";
        document.getElementById("pc" + String(i)).style.color = "rgba(96, 106, 119, 1)";
    }
    document.getElementById("book").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("book").style.color = "white";
    document.getElementById("book").innerText = "Book For: 5.99₾";
}

// Functions to select parking options
function selectPC4() {
    // Change styles to highlight the fourth parking option
    document.getElementById("pc4").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("pc4").style.color = "white";
    for (let i = 1; i <= 4; i++) {
        if (i == 4) {
            continue;
        }
        document.getElementById("pc" + String(i)).style.backgroundColor = "rgba(34, 39, 46, 0.6)";
        document.getElementById("pc" + String(i)).style.color = "rgba(96, 106, 119, 1)";
    }
    document.getElementById("book").style.backgroundColor = "rgba(82, 136, 159, 1)";
    document.getElementById("book").style.color = "white";
    document.getElementById("book").innerText = "Book For: 5.99₾";
}