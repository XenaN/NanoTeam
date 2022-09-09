class Api {
  constructor() {
    // this._url = 'http://127.0.0.1:8000'
    this._url = 'http://77.222.42.233'
  }

  _checkResponse(res) {
    if (res.ok) {
      return res.json();
    }
    return Promise.reject(`Ошибка: ${res.status}`);
  }

  getPredict(material, coat_functional_froup, concentration, shape, time,
    cell_tissue, size_in_water, cell_motphology, cell_age, cell_line, cell_type, no_of_cells,
    zeta_in_water, diameter, cell_source) {
    return fetch(this._url + '/model', {
      method: 'POST',
      body: JSON.stringify({
        material, coat_functional_froup, concentration, shape, time,
        cell_tissue, size_in_water, cell_motphology, cell_age, cell_line, cell_type, no_of_cells,
        zeta_in_water, diameter, cell_source
      }),
      headers: { 'Content-type': 'application/json' }
    })
      .then(this._checkResponse)
  }

  getFeatures() {
    return fetch(this._url + '/features', {
      method: 'GET',
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
const formInputCoatFunctionalFroup = form.querySelector('.input__input-text[name=input-coat_functional_froup]')
const formInputConcentration = form.querySelector('.input__input-text[name=input-concentration]')
const formInputShape = form.querySelector('.input__input-text[name=input-shape]')
const formInputTime = form.querySelector('.input__input-text[name=input-time]')
const formInputCellTissue = form.querySelector('.input__input-text[name=input-cell_tissue]')
const formInputSizeInWater = form.querySelector('.input__input-text[name=input-size_in_water]')
const formInputCellMotphology = form.querySelector('.input__input-text[name=input-cell_motphology]')
const formInputCellAge = form.querySelector('.input__input-text[name=input-cell_age]')
const formInputCellLine = form.querySelector('.input__input-text[name=input-cell_line]')
const formInputCellType = form.querySelector('.input__input-text[name=input-cell_type]')
const formInputNoOfCells = form.querySelector('.input__input-text[name=input-no_of_cells]')
const formInputZetaInWater = form.querySelector('.input__input-text[name=input-zeta_in_water]')
const formInputDiameter = form.querySelector('.input__input-text[name=input-diameter]')
const formInputCellSource = form.querySelector('.input__input-text[name=input-cell_source]')

const threshold = document.querySelector('.input__input-text[name=threshold]')
const thresholdPolzunok = document.querySelector('.input__input-text[name=threshold-polzunok]')

const result = document.querySelector('.input__result')
const resultImg = document.querySelector('.input__result-img')

const resultGoodText = ""
const resultGoodImg = "./images/smile-alive.png"
const resultBadText = ""
const resultBadImg = "./images/smile-dead.png"


form.addEventListener('submit', (evt) => {
  evt.preventDefault()

  const material = formInputMaterial.value
  const coat_functional_froup = formInputCoatFunctionalFroup.value
  const concentration = formInputConcentration.value
  const shape = formInputShape.value
  const time = formInputTime.value
  const cell_tissue = formInputCellTissue.value
  const size_in_water = formInputSizeInWater.value
  const cell_motphology = formInputCellMotphology.value
  const cell_age = formInputCellAge.value
  const cell_line = formInputCellLine.value
  const cell_type = formInputCellType.value
  const no_of_cells = formInputNoOfCells.value
  const zeta_in_water = formInputZetaInWater.value
  const diameter = formInputDiameter.value
  const cell_source = formInputCellSource.value

  api.getPredict(material, coat_functional_froup, concentration, shape, time,
    cell_tissue, size_in_water, cell_motphology, cell_age, cell_line, cell_type, no_of_cells,
    zeta_in_water, diameter, cell_source)
    .then(res => {
      if (res || res === 0) {
        scoreValue = res
        if (res < 0) {
          scoreValue = 0
        }
        if (res > 100) {
          scoreValue = 100
        }
        score.textContent = String(Number(scoreValue).toFixed(2))
        scoreContainer.classList.add(activeClass)

        if (Number(scoreValue) >= Number(threshold.value)) {
          result.textContent = resultGoodText
          resultImg.src = resultGoodImg
        }
        else {
          result.textContent = resultBadText
          resultImg.src = resultBadImg
        }

        scoreContainer.scrollIntoView(false)
      }
    })
})

function checkMinMaxValue(element) {
  element.addEventListener('blur', () => {
    const minValue = element.getAttribute('min')
    const maxValue = element.getAttribute('max')

    if (Number(element.value) < Number(minValue)) {
      element.value = minValue
    }
    if (Number(element.value) > Number(maxValue)) {
      element.value = maxValue
    }
  })
}

checkMinMaxValue(formInputConcentration)
checkMinMaxValue(formInputTime)
checkMinMaxValue(formInputSizeInWater)
checkMinMaxValue(formInputNoOfCells)
checkMinMaxValue(formInputZetaInWater)
checkMinMaxValue(formInputDiameter)
checkMinMaxValue(threshold)

const catFeatures = {
  'coat_functional_froup': formInputCoatFunctionalFroup,
  'shape': formInputShape,
  'material': formInputMaterial,
  'cell_tissue': formInputCellTissue,
  'cell_motphology': formInputCellMotphology,
  'cell_age': formInputCellAge,
  'cell_line': formInputCellLine,
  'cell_type': formInputCellType,
  'cell_source': formInputCellSource
}

const numFeatures = {
  'concentration': formInputConcentration,
  'time': formInputTime,
  'size_in_water': formInputSizeInWater,
  'no_of_cells': formInputNoOfCells,
  'zeta_in_water': formInputZetaInWater,
  'diameter': formInputDiameter
}

api.getFeatures()
  .then(res => {
    if (res) {
      const features = res

      catFeaturesList = Array.from(Object.keys(catFeatures))
      numFeaturesList = Array.from(Object.keys(numFeatures))

      featuresKeys = Array.from(Object.keys(features))
      // console.log(featuresKeys)
      // console.log(catFeaturesList)
      // console.log(catFeaturesList.includes(featuresKeys[0]))
      featuresKeys.forEach(item => {

        if (catFeaturesList.includes(item)) {
          const thisElement = catFeatures[item]
          if (thisElement) {
            const option = thisElement.querySelector('option')
            features[item].forEach((featureItem, index) => {
              const newObject = option.cloneNode(true)
              newObject.textContent = featureItem
              newObject.value = featureItem
              thisElement.append(newObject)
            })
            option.disabled = 'True'
          }
        }

        if (numFeaturesList.includes(item)) {
          const thisElement = numFeatures[item]
          const thisElementRange = thisElement.closest('label').querySelector('input[type=range]')
          thisElement.min = features[item][0]
          thisElementRange.min = features[item][0]
          thisElement.max = features[item][1]
          thisElementRange.max = features[item][1]
          thisElementRange.defaultValue = (features[item][0] + features[item][1]) / 2
        }
      })

    }
  })

const inputNumberList = Array.from(form.querySelectorAll('.input__input-text[type=number]'))
const inputRangeList = Array.from(form.querySelectorAll('.input__input-text[type=range]'))
inputNumberList.forEach((item, index) => {
  item.addEventListener('change', () => {
    inputRangeList[index].value = item.value
  })
})
inputRangeList.forEach((item, index) => {
  item.addEventListener('input', () => {
    inputNumberList[index].value = item.value
  })
})

threshold.addEventListener('change', () => {
  thresholdPolzunok.value = threshold.value
  if (Number(score.textContent) >= threshold.value) {
    result.textContent = resultGoodText
    resultImg.src = resultGoodImg
  }
  else {
    result.textContent = resultBadText
    resultImg.src = resultBadImg
  }
})


thresholdPolzunok.addEventListener('input', () => {
  threshold.value = thresholdPolzunok.value
  if (Number(score.textContent) >= threshold.value) {
    result.textContent = resultGoodText
    resultImg.src = resultGoodImg
  }
  else {
    result.textContent = resultBadText
    resultImg.src = resultBadImg
  }
})

