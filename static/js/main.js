// Menú móvil
const boton = document.getElementById('menuBoton');
const menu = document.getElementById('menu');
if (boton && menu) {
  boton.addEventListener('click', () => {
    const abierto = menu.classList.toggle('menu--abierto');
    boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
  });
}

// Menú desplegable "Productos"
const desplegable = document.getElementById('desplegable');
const desplegableBoton = document.getElementById('desplegableBoton');
if (desplegable && desplegableBoton) {
  const abrir = (estado) => {
    desplegable.classList.toggle('desplegable--abierto', estado);
    desplegableBoton.setAttribute('aria-expanded', estado ? 'true' : 'false');
  };
  desplegableBoton.addEventListener('click', (e) => {
    e.stopPropagation();
    abrir(!desplegable.classList.contains('desplegable--abierto'));
  });
  document.addEventListener('click', (e) => { if (!desplegable.contains(e.target)) abrir(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') abrir(false); });
  desplegable.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => {
    abrir(false);
    if (menu) menu.classList.remove('menu--abierto');
  }));
}

// Sombra de la cabecera al hacer scroll
const cabecera = document.getElementById('cabecera');
window.addEventListener('scroll', () => {
  cabecera.classList.toggle('cabecera--scroll', window.scrollY > 10);
});
