// RESTORE DARK MODE

window.onload = function () {

    if (
        localStorage.getItem("darkMode")
        === "enabled"
    ) {

        document.body.classList.add(
            "dark-mode"
        );

    }

};

// LOADING STATE

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.querySelector("form");

        if (form) {

            form.addEventListener(
                "submit",
                function () {

                    const loader =
                        document.getElementById(
                            "loader"
                        );

                    const button =
                        document.getElementById(
                            "generateBtn"
                        );

                    if (loader) {

                        loader.style.display =
                            "block";

                    }

                    if (button) {

                        button.innerText =
                            "Generating...";

                    }

                }
            );

        }

    }
);

// TOGGLE DARK MODE

function toggleDarkMode() {

    document.body.classList.toggle(
        "dark-mode"
    );

    if (
        document.body.classList.contains(
            "dark-mode"
        )
    ) {

        localStorage.setItem(
            "darkMode",
            "enabled"
        );

    }

    else {

        localStorage.setItem(
            "darkMode",
            "disabled"
        );

    }

}

// COPY FUNCTION

function copyText(id) {

    let text =

        document.getElementById(id)
            .innerText;

    navigator.clipboard.writeText(text);

    alert("Copied successfully!");

}

// DOWNLOAD FUNCTION

function downloadContent() {

    let captions =

        document.getElementById(
            "captionsBox"
        ).innerText;

    let hashtags =

        document.getElementById(
            "hashtagsBox"
        ).innerText;

    let ideas =

        document.getElementById(
            "ideasBox"
        ).innerText;

    let fullContent =

        "=== LAF AI GENERATED CONTENT ===\n\n" +

        "CAPTIONS:\n" +
        captions +

        "\n\nHASHTAGS:\n" +
        hashtags +

        "\n\nIDEAS:\n" +
        ideas;

    let blob = new Blob(

        [fullContent],

        { type: "text/plain" }

    );

    let link =

        document.createElement("a");

    link.href =

        URL.createObjectURL(blob);

    link.download =

        "laf_ai_content.txt";

    link.click();

}