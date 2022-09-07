class Api {
  constructor() {
    this._url = 'http://127.0.0.1:8000'
  }

  _checkResponse(res) {
    if (res.ok) {
      return res.json();
    }
    return Promise.reject(`Ошибка: ${res.status}`);
  }

  getPredict(material, hydro_size, cell_line, time, dose) {
    return fetch(this._url + '/model', {
      method: 'POST',
      body: JSON.stringify({
        material, hydro_size, cell_line, time, dose
      }),
      headers: { 'Content-type': 'application/json' }
    })
      .then(this._checkResponse)
  }
}

const api = new Api()

const activeClass = 'input__score-cont_type_visible'
const scoreContainer = document.querySelector('.input__score-cont')
const score = scoreContainer.querySelector('.input__score')

const form = document.querySelector('.input__form')
const formInputMaterial = form.querySelector('.input__input-text[name=input-material]')
const formInputHydroSize = form.querySelector('.input__input-text[name=input-hydro_size]')
const formInputCellLine = form.querySelector('.input__input-text[name=input-cell_line]')
const formInputTIme = form.querySelector('.input__input-text[name=input-time]')
const formInputDose = form.querySelector('.input__input-text[name=input-dose]')

form.addEventListener('submit', (evt) => {
  evt.preventDefault()
  material = formInputMaterial.value
  hydro_size = formInputHydroSize.value
  cell_line = formInputCellLine.value
  time = formInputTIme.value
  dose = formInputDose.value

  api.getPredict(material, hydro_size, cell_line, time, dose)
    .then(res => {
      if(res) {
        score.textContent = String(res)
        scoreContainer.classList.add(activeClass)
      }
    })
})