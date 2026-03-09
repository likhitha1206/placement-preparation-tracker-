function updateProgress() {
    const total = document.querySelectorAll('input[type="checkbox"]').length;
    const checked = document.querySelectorAll('input[type="checkbox"]:checked').length;

    let percent = 0;
    if (total > 0) {
        percent = Math.round((checked / total) * 100);
    }

    document.getElementById("progressText").innerText = percent + "%";
    document.getElementById("progressFill").style.width = percent + "%";
}