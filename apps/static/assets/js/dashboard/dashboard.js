document.addEventListener("DOMContentLoaded", function () {
  Dropzone.autoDiscover = false;

  if (Dropzone.instances.length === 0) {
    const myDropzone = new Dropzone("#my-dropzone", {
      url: "/dashboard/",
      maxFilesize: 5,
      acceptedFiles: ".xlsx,.csv",
      addRemoveLinks: true,
      success: function(file, response) {
        alert("Successfully uploaded!");
        this.removeFile(file);
      },
      removedfile: function(file) {
        file.previewElement.remove();
      }
    });
  }
});
