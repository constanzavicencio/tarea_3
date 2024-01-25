const validarDeportes = (deportes) => {
    if (deportes=="") return false;

    var options = document.getElementById('deportes').options, count = 0;
    for (var i=0; i < options.length; i++) {
      if (options[i].selected) count++;
    }

    let lengthValid = 1 <= count && count <= 3;

    return lengthValid;
};

const validarRegion = (region) => {
    if (region=="sin-region") return false;
    else return true;
};

const validarComuna = (comuna) => {
    if (comuna=="sin-comuna") return false;
    else return true;
};

const validarTransporte = (transporte) => {
    if (transporte=="") return false;
    else return true;
};

const validarNombre = (nombre) => {
    if (!nombre) return false;

    let lengthValid = 3 <= nombre.length && nombre.length <= 80;

    let re = /^[A-Za-z]{3,80}$/;
    let formatValid = re.test(nombre);

    return lengthValid && formatValid;
};

const validarEmail = (email) => {
    if (!email) return false;

    let for1 = /^[\w.]+@[a-zA-Z]{2,}\.[a-zA-Z]{2,3}$/; // sin subdominio
    let for2 = /^[a-zA-Z0-9.]+@[a-zA-Z]{2}\.[a-zA-Z]{2,}\.[a-zA-Z]{2,3}$/;
    let formatValid = for1.test(email) || for2.test(email);

    return formatValid;
};

const validarNumero = (numero) => {
    if (numero) {
        let re = /^[+]56 9 [0-9]{4} [0-9]{4}$/;
        let formatValid = re.test(numero); 

        return formatValid;
    } else return true;
};

const validarForm = () => {
    console.log("Comienza validación en JavaScript")
    let formHincha = document.forms["formulario-hincha"];
    let deportes = formHincha.deportes.value;
    let region = formHincha.regiones.value;
    let comuna = formHincha.comunas.value;
    let transporte = formHincha.transporte.value;
    let nombre = formHincha.nombre.value;
    let email = formHincha.email.value;
    let numero = formHincha.numero.value;

    console.log(deportes)
    console.log(region)
    console.log(comuna)

    let invalidInputs = [];
    let isValid = true;

    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid = false;
    };

    if (!validarDeportes(deportes)) {
        setInvalidInput("Deportes");
    } 
    if (!validarRegion(region)) {
        setInvalidInput("Región");
    } 
    if (!validarComuna(comuna)) {
        setInvalidInput("Comuna");  
    } 
    if (!validarTransporte(transporte)) {
        setInvalidInput("Modo de transporte");  
    } 
    if (!validarNombre(nombre)) {
        setInvalidInput("Nombre");
    } 
    if (!validarEmail(email)) {
        setInvalidInput("Email de contacto");
    } 
    if (!validarNumero(numero)) {
        setInvalidInput("Número de contacto");
    }

    console.log("Continúa validación en JavaScript")

    let validationBox = document.getElementById("val-box");
    let validationListElem = document.getElementById("val-list");
    validationListElem.innerText = "Los siguientes campos son inválidos: ";

    let sentBox = document.getElementById("sent-box");

    console.log("Se está por enviar el formulario")

    const enviarForm = () => {
        console.log("La función enviarForm se está ejecutando...")
        let formHincha = document.forms["formulario-hincha"];
        sentBox.hidden = false;
        //formHincha.submit()
        formHincha.submit(function(e) {
            e.preventDefault();
        });
    };

    const cerrarPopup = () => {
        document.querySelector('.popup').style.display = 'none';
    };

    if (!isValid) {
        console.log("No es válido")
        let invalidInputsLower = invalidInputs.map(elemento => elemento.toLowerCase());
        let invalidInputsString = invalidInputsLower.join(', ');
        validationListElem.innerText += invalidInputsString;

        // make validation prompt visible
        validationBox.hidden = false;

    } else if (isValid) {
        console.log("Es válido")
        document.querySelector('.popup').style.display = 'block';

        let confirmationBtn = document.getElementById("confirmation-btn");
        confirmationBtn.addEventListener("click", enviarForm);

        console.log(nombre, region, comuna, numero)
        
        let cancelBtn = document.getElementById("cancel-btn");
        cancelBtn.addEventListener("click", cerrarPopup)
    }
};

let submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", validarForm);
