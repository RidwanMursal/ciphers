// constants
const ceasarDesc = `
The ceaser cipher is a simple substitution cipher which shifts a base string of characters to the left or right n times ( where n = key ). When given a plaintext, each letter in the plaintext is first found in the original base string, and is given a new value based on it's corresponding character in the shifted string. <br><br>

<span class="key-info"> The key must be a non negative integer </span>. <br><br>

Ex: plaintext: hello, key: 3, base: abcdefghijklmnopqrstuvwxyz (the alphapet) <br><br>

First, we will find the new base; that is the original base with a left shift of three. <br><br>

new_base: defghijklmnopqrstuvwxyzabc <br><br>

Lastly, we change each letter of our plaintext to match the corresponding letter in the shifted base. <br><br>

h -> k,<br>
e -> h,<br>
l -> o,<br>
l -> o,<br>
o -> r <br><br>

Thus the encrypted cipher text will result in khoor. The decryption process uses the same key, and implements this process in reverse. 
`;

const columnarDesc = `
<span class="key-info">The key value for the Columnar transposition cipher is any string consisting of 2 or more unique letters</span>. These letters will be transformed into a permutation based on the order of each letter in the string. ie ray => [2, 1, 3], as a appears before r in the alphabet, and r appears before y.<br><br>

The columnar transposition cipher works by first writing out the plaintext in a matrix based on the key value. The amount of columns the matrix has will correspond to the length of the key. For instance, for the key ray, the corresponding matrix will have 3 columns. If there are empty cells in the matrix, they will be filled with a pad of q.<br><br>

Ex plaintext: hello, key: ray -> [2, 1, 3] <br><br> 

[h, e, l]<br>
[l, o, q]<br><br>

Next, we encrypt the text by rearranging the matrix based on the permutation we've recieved from the key. In the above example, since the key gives us the permutation [2, 1, 3], we will swap the first column's contents with second column's contents.<br><br>

Ex plaintext: hello, key: ray -> [2, 1, 3] <br><br> 

[e, h, l]<br>
[o, l, q]<br><br>

Thus we now have our cipher text, eohllq. The decryption process is similar, but in reverse. 
`;

const vdesc = `The Vigenere Cipher implemented here uses a running key. To best understand this we must first visualize a table of the alphabet with 26 rows, each row being the alphabet with a left shift of n, where n is the row number (take a look at the table below). <br><br>

Next, we have to make sure our key is a character of strings who's length is equal to the plaintext. We do this by repeating the key until key length = plaintext length. Then, for each letter in the plaintext, we find the corresponding ciphertext letter by looking at the table entry where the column is equal to the plaintext's letter, and the row is equal to the key's letter. We do this for every letter in the plaintext and key. <br><br>

Ex plaintext: fade, key: cab <br><br>

1) Because key is of length 3, and plaintext is of length 4, we must repeat the key enough times so that it matches the length of the plaintext. Thus, the new key is "cabc" <br><br>

2) Make a table like the one described above.  For simplicity, we will use an alphabet with only 5 letters as it is easier to display. <br><br>

    <span class="ml-lg">[a, b, c, d, e,  f]</span> <br><br>

a,    <span class="ml">[a, b, c, d, e, f]</span> <br>
b,    <span class="ml">[b, c, d, e, f, a]</span> <br>
c,    <span class="ml">[c, d, e, f, a, b]</span> <br>
d,    <span class="ml">[d, e, f, a, b, c]</span> <br>
e,    <span class="ml">[e, f, a, b, c, e]</span> <br>
f,    <span class="ml">[f, a, b, c, d, e]</span> <br><br>

3) Since the first letter in the plaintext is "f" and the first letter in our key is "c", we simply need to look in the f column and find the corresponding value in the c row. This gives us a value of b. 
This will be the first letter in our ciphertext.<br><br> 

    <span class="ml-lg">[a, b, c, d, e,  f]</span> <br><br>

a,    <span class="ml">[a, b, c, d, e, f]</span> <br>
b,    <span class="ml">[b, c, d, e, f, a]</span> <br>
c,    <span class="ml">[c, d, e, f, a, <span class="bold">b</span>]</span> <br>
d,    <span class="ml">[d, e, f, a, b, c]</span> <br>
e,    <span class="ml">[e, f, a, b, c, e]</span> <br>
f,    <span class="ml">[f, a, b, c, d, e]</span> <br><br>

4) Repeat this for all letters in the plaintext<br><br> 

    <span class="ml-lg">[a, b, c, d, e,  f]</span> <br><br> 

a,    <span class="ml">[<span class="bold">a</span>, b, c, d, e, f]</span> <br>
b,    <span class="ml">[b, c, d, e, f, a]</span> <br>
c,    <span class="ml">[c, d, e, f, a, b]</span> <br>
d,    <span class="ml">[d, e, f, a, b, c]</span> <br>
e,    <span class="ml">[e, f, a, b, c, e]</span> <br>
f,    <span class="ml">[f, a, b, c, d, e]</span> <br><br>

    <span class="ml-lg">[a, b, c, d, e,  f]</span> <br><br> 

a,    <span class="ml">[a, b, c, d, e, f]</span> <br>
b,    <span class="ml">[b, c, d, <span class="bold">e</span>, f, a]</span> <br>
c,    <span class="ml">[c, d, e, f, a, b]</span> <br>
e,    <span class="ml">[e, f, a, b, c, e]</span> <br>
f,    <span class="ml">[f, a, b, c, d, e]</span> <br><br>

    <span class="ml-lg">[a, b, c, d, e,  f]</span> <br><br> 

a,    <span class="ml">[a, b, c, d, e, f]</span> <br>
b,    <span class="ml">[b, c, d, e, f, a]</span> <br>
c,    <span class="ml">[c, d, e, f, <span class="bold">a</span>, b]</span> <br>
d,    <span class="ml">[d, e, f, a, b, c]</span> <br>
e,    <span class="ml">[e, f, a, b, c, e]</span> <br>
f,    <span class="ml">[f, a, b, c, d, e]</span> <br><br>

5) The resulting ciphertext is <span class="bold"> baea </span>
`;
document.querySelector(".ceasar-desc").innerHTML = ceasarDesc;
document.querySelector(".columnar-desc").innerHTML = columnarDesc;
document.querySelector(".vigenere-desc").innerHTML = vdesc;

function removeErrors() {
  document.querySelector(".error").classList.add("hidden");
}
/**
 * Sends required data to backend and
 * Updates the result textarea based
 * On result.
 * @param {boolean} encryptFlag
 * @param {string} method
 * @param {string} key
 */
function sendData(encryptFlag, method, key) {
  // remove any error messages
  removeErrors();

  const userInput = document.querySelector("#user_input").value;
  const result = document.querySelector("#result");

  const requestData = {
    userInput,
    key,
    encryptFlag,
  };
  console.log(method);
  console.log(requestData);
  console.log(JSON.stringify(requestData));

  fetch(`http://localhost:5000/${method}`, {
    body: JSON.stringify(requestData),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      result.value = data.text;
    })
    .catch((error) => console.log(error));
}

/**
 * Dispatches to key check functions
 * Depending on the cipher specified by the user.
 * @param {boolean} flag - Either encrypt or decrypt
 */
function keyCheckDispatcher(flag) {
  const method = document
    .querySelector("#ciphers")
    [document.querySelector("#ciphers").selectedIndex].innerHTML.toLowerCase()
    .replaceAll(" ", "_");

  if (method === "columnar_transposition_cipher") {
    keyCheckColumnar(method, flag);
  } else if (method === "vigenere_cipher") {
    keyCheckVigenere(method, flag);
  } else if (method === "ceasar_cipher") {
    console.log(method);
    keyCheckCeasar(method, flag);
  }
}

/**
 * Checks if key given is numeric.
 * @param {string} key
 * @returns {boolean}
 */
function isNumeric(key) {
  for (let i = 0; i < key.length; i++) {
    code = key.charCodeAt(i);
    if (!(code > 47 && code < 58)) return false; // numeric (0-9)
  }
  return true;
}

/**
 * Validates a ceaser cipher key.
 * Key must be a positive integer.
 * If valid, send data is called.
 * @param {string} method
 * @param {boolean} flag
 */

function keyCheckCeasar(method, flag) {
  console.log("in key check ceasar");
  const key = document.querySelector("#key").value;

  if (!isNumeric(key)) {
    const errorMessage = document.querySelector(".error");
    errorMessage.classList.remove("hidden");
    errorMessage.innerHTML = "Please ensure your key is a positive integer";
  } else sendData(flag, method, key);
}

/**
 * Validates a columnar cipher key.
 * Key must be at least two unique characters.
 * If valid, send data is called.
 * @param {*} method
 * @param {*} flag
 */

function keyCheckColumnar(method, flag) {
  console.log("in key check columnar");
  const key = document.querySelector("#key").value;
  if (key.length < 2 || key.replaceAll(key[0], "") === "") {
    const errorMessage = document.querySelector(".error");
    errorMessage.classList.remove("hidden");
  } else sendData(flag, method, key);
}

/**
 * Checks if a key contains a single alpha character.
 * @param {string} key
 * @returns {boolean}
 */
function hasAlpha(key) {
  for (let i = 0; i < key.length; i++) {
    code = key.charCodeAt(i);
    if (
      (code > 64 && code < 91) || // upper alpha (A-Z)
      (code > 96 && code < 123)
    ) {
      // lower alpha (a-z)
      return true;
    }
    return false;
  }
}

/**
 * Validates that a key is a valid Vigenere
 * Cipher key. A valid key is one that has
 * at least one alpha character.
 * @param {string} method
 * @param {boolean} flag
 */
function keyCheckVigenere(method, flag) {
  console.log("in vigenere key check");
  const key = document.querySelector("#key").value;
  if (!hasAlpha(key)) {
    const errorMessage = document.querySelector(".error");
    errorMessage.classList.remove("hidden");
    errorMessage.innerHTML =
      "Please ensure your key contains one alpha character.";
  } else sendData(flag, method, key);
}

document.querySelectorAll(".desc-header-container").forEach((cipher) => {
  cipher.addEventListener("click", () => {
    const expanded = cipher.dataset.expanded;
    const description = cipher.children[1];

    description.classList.remove("hidden");
    console.log("YOOOOOOOOO");
    description.addEventListener("animationend", (event) => {
      console.log("IN DESCRIPTION ON CLICK, EXPANDED HERE IS: ", expanded);
      console.log(event);
      if (event.animationName === "fade-out") {
        description.classList.remove("fade-out");
        description.classList.add("hidden");
      } else {
        description.classList.remove("fade-in");
      }
    });
    // play animation
    console.log("general expanded is, ", expanded);
    if (expanded == "false") description.classList.add("fade-in");
    else description.classList.add("fade-out");

    cipher.dataset.expanded = expanded === "true" ? "false" : "true";
    console.log(" THIS IS CIPHER.DATASET.EXPANDED", cipher.dataset.expanded);
  });
});

// add event listeners for the encrypt/decrypt buttons
const encryptButton = document.querySelector("#encrypt");
const decryptButton = document.querySelector("#decrypt");

encryptButton.addEventListener("click", () => keyCheckDispatcher("encrypt"));
decryptButton.addEventListener("click", () => keyCheckDispatcher("decrypt"));
