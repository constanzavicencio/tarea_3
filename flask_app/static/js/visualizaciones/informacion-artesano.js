const urlParams = new URLSearchParams(window.location.search);
const id = urlParams.get('id');

const artesanos = {
    '1': {
        nombre: 'Agustín',
        telefono: '+56 9 8542 6723',
        email: 'agustinymetales@gmail.com',
        comuna: 'Providencia',
        region: 'Región Metropolitana',
        tipoArtesanias: 'Metal',
        descripcionArtesanias: 'Bellas artesanías de metal, distintos diseños disponibles.',
        foto: './imagenes/metal.png'
        },
    '2': {
        nombre: 'Martina',
        telefono: '+56 9 7061 3985',
        email: 'martina@maderaschile.cl',
        comuna: 'Sasntiago Centro',
        region: 'Región Metropolitana',
        tipoArtesanias: 'Madera',
        descripcionArtesanias: '',
        foto: './imagenes/madera-1.png'
        },
    '3': {
        nombre: 'Isidora',
        telefono: '+56 9 7120 5498',
        email: 'isidora1008@gmail.com',
        comuna: 'Talca',
        region: 'Región del Maule',
        tipoArtesanias: 'Madera',
        descripcionArtesanias: '',
        foto: './imagenes/madera-2.png'
        },
    '4': {
        nombre: 'Víctor',
        telefono: '+56 9 6304 8112',
        email: 'victorartesano@gmail.com',
        comuna: 'Temuco',
        region: 'Región de La Auraucanía',
        tipoArtesanias: 'Mármol',
        descripcionArtesanias: 'Diseños de todo tipo',
        foto: './imagenes/marmol.png'
        },
    '5': {
        nombre: 'Nicolás',
        telefono: '+56 9 8753 2461',
        email: 'nico1010@gmail.com',
        comuna: 'Temuco',
        region: 'Región de La Araucanía',
        tipoArtesanias: 'Joyas',
        descripcionArtesanias: 'Artesanías mapuches',
        foto: './imagenes/joyas.png'
        },
};

const artesano = artesanos[id];

if (artesano) {
    document.write(`<p><strong>Nombre:</strong> ${artesano.nombre}</p>`);
    document.write(`<p><strong>Teléfono:</strong> ${artesano.telefono}</p>`);
    document.write(`<p><strong>Email:</strong> ${artesano.email}</p>`);
    document.write(`<p><strong>Comuna:</strong> ${artesano.comuna}</p>`);
    document.write(`<p><strong>Región:</strong> ${artesano.region}</p>`);
    document.write(`<p><strong>Tipo de Artesanías:</strong> ${artesano.tipoArtesanias}</p>`);
    if (artesano.descripcionArtesanias != '') {
    document.write(`<p><strong>Descripción artesanías:</strong> ${artesano.descripcionArtesanias}</p>`);
    }
    document.write(`
    <div class="img-container">
        <img class="img" src="${artesano.foto}" width="640" height="480" alt="Artesano">
    </div>
    `);
} else {
    document.write('<p>No se encontró información para el artesano con el ID proporcionado.</p>');
}