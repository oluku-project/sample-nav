const btns = document.querySelectorAll('.tab-btn')
const about = document.querySelector('.about')
const articles = document.querySelectorAll('.content')
const btn = document.getElementById('machine-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBox = document.getElementById('alert-box')

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

const handleAlerts = (type, msg) => {
	alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#myDropZone', {
	url: 'excel_upload/',
	maxFiles: 3,
	maxFileSize: 10,
	acceptedFiles: '.xlsx',
	addRemoveLinks: true,
	init: function () {
		this.on('sending', function (file, xhr, formData) {
			console.log('sending okay')
			formData.append('csrfmiddlewaretoken', csrf)
		}) // sending
		this.on('success', function (file, response) {
			console.log(file, '--', response)
			if (response.ex) {
				handleAlerts('danger', 'File already exists')
			} else {
				handleAlerts('success', 'Your file has been uploaded')
			}
		}) // success file
	}, // init
})
