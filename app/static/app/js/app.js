const linkInput = document.querySelector('input[name="url"]');
const recognizeText = document.querySelector('textarea[name="recognize_text"]');
const pastBtn = document.querySelector('input[name="past_btn"]');
const copyBtn = document.querySelector('input[name="copy_btn"]');

pastBtn.addEventListener('click', () => {
    navigator.clipboard.readText()
        .then(text => {
            console.log(text)
            linkInput.value = text;
        })
        .catch(error => {
            console.log(error)
        })
});

copyBtn.addEventListener('click', () => {
    const text_copy = recognizeText.textContent;
    if (text_copy) {
        navigator.clipboard.writeText(text_copy)
            .then(() => {
                if (copyBtn.value !== 'Copied') {
                    const originalValue = copyBtn.value;
                    copyBtn.value = 'Copied';
                    setTimeout(() => {
                        copyBtn.value = originalValue
                    }, 1500);
                }
            })
            .catch(error => {
                console.log(error);
            })
    }
});


