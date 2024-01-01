
        function previewImage(input, index) {
            const files = input.files;
            const imageContainer = document.getElementById(`image-preview-${index}`);
            const image = imageContainer.querySelector('img');

            if (files.length > 0) {
                const file = files[0];
                if (file.type.startsWith('image/')) {
                    image.src = window.URL.createObjectURL(file);
                    imageContainer.querySelector('.cancel-button').onclick = function () {
                        image.src = '';
                    };
                }
            } else {
                image.src = '';
            }
        }
