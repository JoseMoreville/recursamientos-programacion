window.onload = () => {
    getDataFromApi()
}
const obj = {
    name: "jose",
    age: 22,
    favoriteFood: ["mango", "pozole", "mole"],
}

const getDataFromApi = () => {
    const button = document.querySelector("button")
    const img = document.createElement("img")
    const container = document.createElement('div')

    button.addEventListener('click', function (e) {
        e.preventDefault();
        fetch('/api/rickymorty')
            .then(async r => await r.json())
            .then(data => {
                    img.src = data.image
                    container.appendChild(img)
                    container.append(`${data.name}`)
                    container.append(`${data.species}`)
                    container.style.display = "flex"
                    container.style.flexDirection = "column"
                    button.parentNode.appendChild(container)
                    }
                )
        }
    )
    return undefined
};