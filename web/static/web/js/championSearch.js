const addChampionToSearch = (champion, container) => {
    const a = document.createElement("a")
    a.href = "/champion/" + champion
    a.className = "champion-item"
    
    const img = document.createElement("img")
    img.src = `https://opgg-static.akamaized.net/meta/images/lol/latest/champion/${champion}.png?image=e_upscale,c_crop,h_103,w_103,x_9,y_9/q_auto:good,f_webp,w_160,h_160&v=1724034092925`
    img.alt = champion

    const span = document.createElement("span")
    span.innerText = champion.charAt(0).toUpperCase() + champion.slice(1)

    a.appendChild(img)
    a.appendChild(span)

    container.appendChild(a)
}

const addChampionToMainPanel = (champion, container) => {
    const a = document.createElement("a")
    a.href = `champion/${champion.name}`

    const img = document.createElement("img")
    img.src = `https://opgg-static.akamaized.net/meta/images/lol/latest/champion/${champion.name}.png?image=e_upscale,c_crop,h_103,w_103,x_9,y_9/q_auto:good,f_webp,w_160,h_160&v=1724034092925`
    img.alt = champion.name

    const span = document.createElement("span")
    span.innerText = champion.name.charAt(0).toUpperCase() + champion.name.slice(1)

    a.appendChild(img)
    a.appendChild(span)

    container.appendChild(a)
}

const mainChampionInput = document.getElementById("main-champion-input")
const championsContainer = document.getElementById("champions-container")

mainChampionInput.addEventListener("input", () => {
    championsContainer.innerHTML = ""
    const searchValue = mainChampionInput.value.toLowerCase()
    const filtredChamps = searchValue === ""
    ? champions
    : champions.filter(champ => champ.name.toLowerCase().startsWith(searchValue))

    filtredChamps.forEach((champ)=> {
        addChampionToMainPanel(champ, championsContainer)
    })
})