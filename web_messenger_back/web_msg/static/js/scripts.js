function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function postData(url = "", data = {}, type) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: type,
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return await response.json();
}

async function postFormData(url = '', formName, type, reload = "false") {
    const form = document.getElementById(formName);

    form.addEventListener('submit', async event => {
        event.preventDefault();

        const formData = new FormData(form);
        
        const plainFormData = Object.fromEntries(formData.entries());

        postData(url, plainFormData, type);

        if (reload == "true") {
            window.location.reload();
        };

    });
}