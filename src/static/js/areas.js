// Создаем карту 
var map = L.map('map').setView([58.08, 55.74], 7);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map);

// Массив слоев карты
let layers = [];

var overpassApiUrl = 'https://overpass-api.de/api/interpreter';

var element = document.querySelector('.leaflet-bottom.leaflet-right');
if (element) {
    element.remove();
}

// Вешаем на каждую кнопку обработку события клика
for (let j = 1; j <= 10; j += 1) {
  console.log(`J counter ${j}`);
  document.getElementById(`button-${j}`).addEventListener('click', function(){
    fetchData(j);
  });
}

// Функция получения данных о предиктах с бэкенда
async function fetchData(id = 0) { // id обозначает порядковый номер дня, на которых мы прогнозируем
  try {
    const response = await fetch(`/getPredicts?id=${id}`);
    const areasNames = await response.json();
    layers.forEach(layer => map.removeLayer(layer)); // Удаляем все слои карты, чтобы они не накладывались при нескольких запросах
    layers = []; // очищаем массив
    for (let i = 0; i < areasNames.length; i += 1) { // Делаем запрос для каждой области для получения карты, если его уже делали, загружаем из кэша
      var overpassQuery = '';
      if (areasNames[i].name === 'Александровский муниципальный округ') { // Существует два таких региона, поэтому уточняем регион
        overpassQuery = `[out:json];relation["name"="${areasNames[i].name}"]["addr:region"="Пермский край"];out geom;`;
      } else {
        overpassQuery = `[out:json];relation["name"="${areasNames[i].name}"];out geom;`;
      }

      fetch(overpassApiUrl + '?data=' + encodeURIComponent(overpassQuery), { cache: "force-cache" })
        .then((response) => response.json())
        .then((data) => {
          var osmData = osmtogeojson(data);
          var geoLayer = L.geoJSON(osmData, { // Добавляем слой на карту из полученных с overpass api данных
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
          }).addTo(map); // Добавляем слой на карту
          layers.push(geoLayer); // Добавляем слой в наш массив слоев
        })
        .catch((error) => console.error('Ошибка:', error));
    }
  } catch (error) {
    console.log('Ошибка:', error);
  }
}

fetchData();