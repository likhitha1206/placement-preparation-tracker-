function toggleSection(id) {
    let section = document.getElementById(id);

    if (section.style.display === "block") {
        section.style.display = "none";
    } else {
        section.style.display = "block";
    }
}

function updateProgress(topic) {

    let checkboxes = document.querySelectorAll(
        `input[onchange="updateProgress('${topic}')"]`
    );

    let checked = 0;

    checkboxes.forEach(cb => {
        if (cb.checked) checked++;
    });

    let percent = Math.round((checked / checkboxes.length) * 100);

    document.getElementById(topic + "Bar").style.width = percent + "%";
    document.getElementById(topic + "Percent").innerText = percent + "%";
}