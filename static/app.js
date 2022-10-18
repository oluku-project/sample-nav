const btns = document.querySelectorAll('.tab-btn')
const about = document.querySelector('.about')
const articles = document.querySelectorAll('.content')

about.addEventListener('click', (e) => {
  const id = e.target.dataset.id
  activeBtn = e.target
  if (id) {
    // remove active from other buttons
    btns.forEach((btn) => {
      btn.classList.remove('active')
     })
     activeBtn.classList.add('active')
     console.log(activeBtn)
     // hide other articles
     articles.forEach((art) => {
         art.classList.remove('active')
     })
    // content to display by id
    const content = document.getElementById(id)
    content.classList.add('active')
  }
})
