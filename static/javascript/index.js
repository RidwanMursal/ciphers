function removeErrors() {
    document.querySelector(".error").classList.add("hidden")
}
// send data function
function sendData(encryptFlag, method, key) {
    // remove any error messages
    removeErrors()

    const userInput = document.querySelector("#user_input").value
    // const key = document.querySelector("#key").value
    // const method = document.querySelector("#ciphers")[document.querySelector("#ciphers").selectedIndex].innerHTML;
    const result = document.querySelector("#result")

    const requestData = {
        userInput, 
        key, 
        encryptFlag,
    }
    console.log(method)
    console.log(requestData)
    console.log(JSON.stringify(requestData))

    fetch(`http://localhost:5000/${method}`, {
        body: JSON.stringify(requestData), 
        method: "POST", 
        headers: {
        'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        result.value = data.text
    }).catch(error => console.log(error))
}

// dispatcher 

function keyCheckDispatcher(flag) {
    
    const method = document.querySelector("#ciphers")[document.querySelector("#ciphers").selectedIndex].innerHTML.toLowerCase().replaceAll(" ", "_");
    
    if (method === "columnar_transposition_cipher") {
        
        keyCheckColumnar(method, flag)

    } else if (method === "vigenere_cipher") {
        keyCheckVigenere(method, flag)
    } else if (method === "ceasar_cipher") {
        console.log(method)
        keyCheckCeasar(method, flag )
    }
    
}


function isNumeric(key) {
    for(let i = 0; i < key.length; i ++) {
        code = key.charCodeAt(i)
        if (!(code > 47 && code < 58) ) return false // numeric (0-9) 
    }
    return true 
}

function keyCheckCeasar(method, flag) {
    console.log("in key check ceasar")
    const key = document.querySelector("#key").value 
    
    if (!isNumeric(key)) {
        const errorMessage = document.querySelector(".error")
        errorMessage.classList.remove("hidden")
        errorMessage.innerHTML = "Please ensure your key is a positive integer"
    }else sendData(flag, method, key)
}

function keyCheckColumnar(method, flag) {
    console.log("in key check columnar")
    const key = document.querySelector("#key").value 
    if (key.length < 2 || key.replaceAll(key[0], "") === "") {
        const errorMessage = document.querySelector(".error")
        errorMessage.classList.remove("hidden")
    } else sendData(flag, method, key)
}

function hasAlpha(key) {
    for (let i = 0; i < key.length; i++ ) {
        code = key.charCodeAt(i);
        if ((code > 64 && code < 91) || // upper alpha (A-Z)
            (code > 96 && code < 123)) { // lower alpha (a-z)
        return true 
        }
    return false 
    }
}

function keyCheckVigenere(method, flag) {
    console.log("in vigenere key check")
    const key = document.querySelector("#key").value 
    if (!hasAlpha(key)) {
        const errorMessage = document.querySelector(".error")
        errorMessage.classList.remove("hidden")
        errorMessage.innerHTML = "Please ensure your key contains one alpha character."
    } else sendData(flag, method, key)
}

// intro stuff 
document.querySelectorAll(".desc-header-container").forEach(cipher => {
    
    cipher.addEventListener("click", () => {
        const expanded = cipher.dataset.expanded 
        const description = cipher.children[1]

        description.classList.remove("hidden")
        console.log("YOOOOOOOOO")
        description.addEventListener("animationend", (event) => {
            // if (expanded === "true") {description.classList.add("hidden"); description.classList.remove("fade-out")}
            // else {description.classList.remove("fade-in")}
            console.log("IN DESCRIPTION ON CLICK, EXPANDED HERE IS: ", expanded)
            console.log(event)
            if (event.animationName === "fade-out")  {
                description.classList.remove("fade-out")
                description.classList.add("hidden")
            } else {
                description.classList.remove("fade-in")
            }
        }) 
        // play animation
        console.log("general expanded is, ", expanded)
        if (expanded == "false") description.classList.add("fade-in") 
        else description.classList.add("fade-out")
        

        cipher.dataset.expanded = ( expanded === "true" ) ? "false":"true"
        console.log(" THIS IS CIPHER.DATASET.EXPANDED", cipher.dataset.expanded)
    })
})

// add event listeners for the encrypt/decrypt buttons 
const encryptButton = document.querySelector("#encrypt")
const decryptButton = document.querySelector("#decrypt")

// sendData("encrypt")
encryptButton.addEventListener("click", () => keyCheckDispatcher("encrypt"))
decryptButton.addEventListener("click", () => keyCheckDispatcher("decrypt"))
console.log(encryptButton)