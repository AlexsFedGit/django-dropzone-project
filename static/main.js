Dropzone.autoDiscover=false;
const myDropzone = new Dropzone('#my-dropzone', {
        url: 'upload/',
        maxFiles: 5,
        maxFilesize: 2,
        acceptedFiles: 'image/*',
        dictDefaultMessage: "Перетащите файлы для загрузки на сайт",
        maxFilesize: 10,
})
