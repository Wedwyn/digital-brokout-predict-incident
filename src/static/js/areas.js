var overpassApiUrl = 'https://overpass-api.de/api/interpreter';

var map = L.map('map').setView([58.08, 55.74], 7);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map);

// let geoLayer = null;
// let layers = L.layerGroup().addTo(map);
let layers = [];

// var areasNames = [
//   { name: 'Краснокамский городской округ', color: 'red' },
//   { name: 'Пермский муниципальный округ', color: 'green' },
//   { name: 'Пермский городской округ', color: 'red' },
//   { name: 'Соликамский городской округ', color: 'red' },
//   { name: 'Кунгурский муниципальный округ', color: 'red' },
//   { name: 'городской округ Березники', color: 'green' },
//   { name: 'Суксунский городской округ', color: 'green' },
//   { name: 'Чайковский городской округ', color: 'green' },
//   { name: 'Чусовской городской округ', color: 'red' },
//   { name: 'Лысьвенский городской округ', color: 'green' },
//   { name: 'Добрянский городской округ', color: 'red' },
//   { name: 'Кудымкарский муниципальный округ', color: 'green' },
//   { name: 'Нытвенский городской округ', color: 'green' },
//   { name: 'Губахинский муниципальный округ', color: 'green' },
//   { name: 'Чернушинский городской округ', color: 'green' },
//   { name: 'Верещагинский городской округ', color: 'green' },
//   { name: 'Октябрьский городской округ', color: 'red' },
//   { name: 'Горнозаводский городской округ', color: 'green' },
//   { name: 'Куединский муниципальный округ', color: 'yellow' },
//   { name: 'Осинский городской округ', color: 'green' },
//   { name: 'городской округ Кизел', color: 'yellow' },
//   { name: 'Красновишерский городской округ', color: 'green' },
//   { name: 'Бардымский муниципальный округ', color: 'red' },
//   { name: 'Карагайский муниципальный округ', color: 'green' },
//   { name: 'Ильинский городской округ', color: 'green' },
//   { name: 'Берёзовский муниципальный округ', color: 'yellow' },
//   { name: 'Юсьвинский муниципальный округ', color: 'green' },
//   { name: 'Чердынский городской округ', color: 'green' },
//   { name: 'Частинский муниципальный округ', color: 'red' },
//   { name: 'Кишертский муниципальный округ', color: 'green' },
//   { name: 'Гайнский муниципальный округ', color: 'red' },
//   { name: 'Большесосновский муниципальный округ', color: 'green' },
//   { name: 'Оханский городской округ', color: 'green' },
//   { name: 'Кочёвский муниципальный округ', color: 'yellow' },
//   { name: 'Ординский муниципальный округ', color: 'green' },
//   { name: 'Очёрский городской округ', color: 'green' },
//   { name: 'Еловский муниципальный округ', color: 'red' },
//   { name: 'Сивинский муниципальный округ', color: 'red' },
//   { name: 'Юрлинский муниципальный округ', color: 'green' },
//   { name: 'Уинский муниципальный округ', color: 'green' },
//   { name: 'Косинский муниципальный округ', color: 'green' },
//   {
//     name: 'Александровский муниципальный округ',
//     color: 'red',
//     popupText: 'Уровень угроз ебанутый, все убегаем',
//   },
// ];
// fetch('/getPredicts');
var element = document.querySelector('.leaflet-bottom.leaflet-right');
if (element) {
    element.remove();
}

for (let j = 1; j <= 10; j += 1) {
  console.log(`J counter ${j}`);
  document.getElementById(`button-${j}`).addEventListener('click', function(){
    fetchData(j);
  });
}

async function fetchData(id = 0) {

  try {
    const response = await fetch(`/getPredicts?id=${id}`);
    const areasNames = await response.json();
    layers.forEach(layer => map.removeLayer(layer));
    layers = []; // очищаем массив
    for (let i = 0; i < areasNames.length; i += 1) {
      var overpassQuery = '';
      if (areasNames[i].name === 'Александровский муниципальный округ') {
        overpassQuery = `[out:json];relation["name"="${areasNames[i].name}"]["addr:region"="Пермский край"];out geom;`;
      } else {
        overpassQuery = `[out:json];relation["name"="${areasNames[i].name}"];out geom;`;
      }

      fetch(overpassApiUrl + '?data=' + encodeURIComponent(overpassQuery), { cache: "force-cache" })
        .then((response) => response.json())
        .then((data) => {
          var osmData = osmtogeojson(data);
          // layers.clearLayers();
          // L.geoJSON(osmData, {...}).addTo(layers);
          // if (geoLayer) map.removeLayer(geoLayer);
          var geoLayer = L.geoJSON(osmData, {
            onEachFeature: function (feature, layer) {
              layer.bindPopup(areasNames[i].popupText);
              layer.bindTooltip(areasNames[i].name);

            },
            style: function (feature) {
              console.log(id);
              if (Number(id) === 4) {
                return { color: `${ i % 3 === 1 ? 'red': i % 3 === 2 ? 'green' : 'yellow'}` }
              } else {
                return { color: `${ i % 3 === 1 ? 'green': i % 3 === 2 ? 'yellow' : 'red'}` };
              }
              // Костыль пока
            },
          }).addTo(map);
          layers.push(geoLayer);
        })
        .catch((error) => console.error('Ошибка:', error));
    }
  } catch (error) {
    console.log('Ошибка:', error);
  }
}

fetchData();