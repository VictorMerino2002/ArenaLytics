const moreItemsBtn = document.getElementById("more-items-btn")
const moreItems = document.getElementById("more-items")
const itemsContainer = document.querySelector(".items")

const prismaticsContainer = document.querySelector(".prismatics")

moreItemsBtn.addEventListener("click", ()=> {
    moreItems.classList.toggle("active")
    itemsContainer.classList.toggle("active")
    prismaticsContainer.classList.toggle("active")

    if (moreItems.classList.contains("active")) {
        moreItemsBtn.innerHTML = '<i class="fa-solid fa-chevron-up"></i>'
    } else {
        moreItemsBtn.innerHTML = '<i class="fa-solid fa-chevron-down"></i>'
    }
})