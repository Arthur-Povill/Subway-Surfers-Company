const substitutionMap = {
    " ": "Z", "Z": " ", ",": "a", "a": ",", "Y": "<", "<": "Y", "*": "/", "/": "*", 
    "\u000b": "F", "F": "\u000b", "N": "5", "5": "N", "D": "l", "l": "D", "+": "m", 
    "m": "+", "S": "W", "W": "S", "|": ";", ";": "|", ">": "_", "_": ">", "e": "j", 
    "j": "e", "%": "p", "p": "%", "6": "L", "L": "6", "7": "H", "H": "7", "~": "U", "U": 
    "~", "h": "k", "k": "h", "1": ")", ")": "1", "w": "T", "T": "w", "O": "A", "A": "O", 
    "[": "y", "y": "[", "v": "q", "q": "v", "c": "$", "$": "c", 
    "g": "}", "}": "g", "E": "M", "M": "E", "o": "?", "?": "o", "G": "u", "u": "G", 
    "!": "R", "R": "!", "-": "Q", "Q": "-", "]": "^", "^": "]", "n": ".", ".": "n", 
    "J": "`", "`": "J", "o": "?", "?": "o", "x": "0", "0": "x", "d": "s", "s": "d", 
    "r": "t", "t": "r", "K": "8", "8": "K", "b": "V", "V": "b", "\\": "@", "@": "\\", 
    "I": ":", ":": "I", "9": "C", "C": "9", "f": "#", "#": "f", "P": "=", "=": "P", 
    "{": "z", "z": "{", "i": "&", "&": "i", "3": "4", "4": "3", "(": "2", "2": "(", 
    "B": "X", "X": "B"
};

function obfuscateMessage(message) {
  let text = '';
  for (const char of message) {
      if (char in substitutionMap) {
          text += substitutionMap[char];
      }else{
            text += char;
      }
  }

  return text;
}

function deobfuscateMessage(message) {
  let text = '';
  for (const char of message) {
      if (char in substitutionMap) {
          text += substitutionMap[char];
      }else{
            text += char;
      }
  }

  return text;
}

function getCSRFToken() {
    const name = 'csrftoken=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i].trim();
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return null;
}

function enabledPopupAlert(alertMessage, alertLink=''){
    if(alertLink !== ''){
        document.getElementById('error-img').setAttribute('src', alertLink);
    }
    document.getElementById('error-message').innerText = alertMessage;
    document.getElementsByClassName('main-alerts')[0].style.display = 'flex';
    document.getElementsByClassName('alert')[0].style.display = 'flex';

}

function enabledLoad(){
    document.getElementsByClassName('alert')[0].style.display = 'none';
    document.getElementsByClassName('main-alerts')[0].style.display = 'flex';
    document.getElementsByClassName('loads')[0].style.display = 'flex';
}

function disabledLoad(){
    document.getElementsByClassName('alert')[0].style.display = 'none';
    document.getElementsByClassName('main-alerts')[0].style.display = 'none';
    document.getElementsByClassName('loads')[0].style.display = 'none';
}

function extractResponseValue(jsonString) {
    const regex = /"response"\s*:\s*"([^"]+)"/;
    const match = jsonString.match(regex);
  
    if (match && match.length >= 2) {
      return match[1];
    } else {
      return null; // A chave "response" não foi encontrada na string JSON
    }
  }

function encodedBase64(message){
    const base64Template = btoa(message.template);
    return base64Template;
}

function decodeBase64(message){
    const originalTemplate = atob(message);
    return originalTemplate;
}

function saveDataInChrome(name, data){
    const storageData = {};
    storageData[name] = data;
    chrome.storage.local.set(storageData, function() {});
}
  
async function loadDataInChrome(name){
    const item = await new Promise(resolve => {
            chrome.storage.local.get(name, function(result) {
                resolve(result);
            });
        });
    return item;
}

function saveDataStorage(name, data){
    localStorage.setItem(name, JSON.stringify(data));
}

function loadDataStorage(name){
    if(localStorage.getItem(name) !== null){
        var status = true;
        var data = JSON.parse(localStorage.getItem(name));
    }else{
        var status = false;
        var data = {};
    }
    return {
        'status': status,
        'data': data
    };
}


export { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, extractResponseValue, encodedBase64, decodeBase64, saveDataInChrome, loadDataInChrome, saveDataStorage, loadDataStorage};