document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const preview = document.getElementById('preview');
    const imagePreview = document.getElementById('imagePreview');
    const processButton = document.getElementById('processButton');
    const results = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');
    const loading = document.getElementById('loading');

    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#007bff';
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = '#ccc';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#ccc';
        
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file');
            return;
        }

        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            preview.hidden = false;
            results.hidden = true;
        };
        reader.readAsDataURL(file);
    }

    processButton.addEventListener('click', async () => {
        const file = fileInput.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        loading.hidden = false;
        processButton.disabled = true;
        results.hidden = true;

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                results.hidden = false;
                resultsContent.innerHTML = `
                    <div class="results-item">
                        <h4>Scene Analysis:</h4>
                        <p>${data.description}</p>
                    </div>
                `;
            } else {
                throw new Error(data.error || 'Processing failed');
            }
        } catch (error) {
            alert(error.message);
        } finally {
            loading.hidden = true;
            processButton.disabled = false;
        }
    });
});