const characters = [
  {
    name: "Yuji Itadori",
    img: STATIC_URL + "src/jjk-yuji.jpg",
    technique: "Divergent Fist",
    desc: "Estudiante de primer año, recipiente de Sukuna. Fuerza sobrehumana y corazón puro."
  },
  {
    name: "Satoru Gojo",
    img: STATIC_URL +"src/jjk-gojo.jpg",
    technique: "Limitless · Six Eyes",
    desc: "El hechicero más fuerte. Manipula el infinito y ve más allá de lo visible."
  },
  {
    name: "Megumi Fushiguro",
    img: STATIC_URL +"src/jjk-megumi.jpg",
    technique: "Ten Shadows",
    desc: "Heredero del clan Zenin. Invoca shikigami desde su sombra."
  },
  {
    name: "Nobara Kugisaki",
    img: STATIC_URL +"src/jjk-nobara.jpg",
    technique: "Straw Doll",
    desc: "Hechicera feroz que usa clavos y un martillo para canalizar energía maldita."
  }
];

const jutsus = [
  {
    jp: "領域展開",
    en: "Domain Expansion",
    desc: "El hechicero materializa su técnica innata en un espacio cerrado."
  },
  {
    jp: "無下限",
    en: "Limitless",
    desc: "Manipulación del espacio infinito entre dos puntos."
  },
  {
    jp: "黒閃",
    en: "Black Flash",
    desc: "Distorsión espacial al impactar con energía maldita en 0.000001s."
  }
];

// Render cards
const cardsContainer = document.getElementById('cards');
cardsContainer.innerHTML = characters.map(c => `
  <article class="card">
    <div class="card-img-wrap">
      <img src="${c.img}" alt="${c.name}" class="card-img" loading="lazy" />
    </div>
    <div class="card-overlay"></div>
    <div class="card-info">
      <p class="card-technique">${c.technique}</p>
      <h3 class="card-name">${c.name}</h3>
      <p class="card-desc">${c.desc}</p>
    </div>
  </article>
`).join('');
