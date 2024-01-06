const validarRegion = (region) => {
    return region !== "sin-region";
};

const validarComuna = (comuna) => {
    return comuna !== "sin-comuna";
};

const validarTipoArtesania = (tipoArtesania) => {
    if (tipoArtesania == "seleccione") return false;
    
    var options = document.getElementById('tipoArtesania').options, count = 0;
    for (var i=0; i < options.length; i++) {
      if (options[i].selected) count++;
    }

    let lengthValid = 1 <= count && count <= 3;

    return lengthValid;
};

const validarImgArtesanias = (imgArtesanias) => {
    const fileList = imgArtesanias.files;
    if (!fileList || fileList.length === 0) return false;

    let lengthValid = 1 <= fileList.length && fileList.length <= 3;

    let typeValid = true;

    for (const file of fileList) {
        typeValid = typeValid && /\.(jpeg|jpg|png)$/i.test(file.name);
    }

    return lengthValid && typeValid;
};

const validarNombre = (nombre) => {
    if (!nombre) return false;

    let lengthValid = 3 <= nombre.length && nombre.length <= 80;

    let formatValid = /^[A-Za-z ]{3,80}$/.test(nombre);

    return lengthValid && formatValid;
};

const validarEmail = (email) => {
    if (!email) return false;

    let formatValid = /^[\w.]+@[a-zA-Z]{2,}\.[a-zA-Z]{2,3}$/.test(email);

    return formatValid;
};

const validarNumero = (numero) => {
    if (numero) {
        let formatValid = /^[+]56 9 [0-9]{4} [0-9]{4}$/.test(numero);
        return formatValid;
    } else {
        return true;
    }
};

const validarForm = () => {
    console.log("Comienza validación en JavaScript")
    let formArtesano = document.forms["formulario-artesano"];
    let region = formArtesano.regiones.value;
    let comuna = formArtesano.comunas.value;
    let nombre = formArtesano.nombre.value;
    let email = formArtesano.email.value;
    let numero = formArtesano.numero.value;
    let tipoArtesania = formArtesano.tipoArtesania.value;
    let imgArtesanias = formArtesano.imgArtesanias;

    let invalidInputs = [];
    let isValid = true;

    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid = false;
    };

    if (!validarRegion(region)) {
        setInvalidInput("Región");
    }
    if (!validarComuna(comuna)) {
        setInvalidInput("Comuna");
    }
    if (!validarTipoArtesania(tipoArtesania)) {
        setInvalidInput("Tipo de Artesanía");
    }
    if (!validarImgArtesanias(imgArtesanias)) {
        setInvalidInput("Fotos de artesanías");
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
        let formArtesano = document.forms["formulario-artesano"];
        sentBox.hidden = false;
        //formArtesano.submit()
        formArtesano.submit(function(e) {
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
