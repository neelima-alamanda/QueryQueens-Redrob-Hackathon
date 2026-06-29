// ============================
// Select HTML Elements
// ============================

const fileInput = document.getElementById("candidateFile");
const rankButton = document.getElementById("rankButton");
const status = document.getElementById("status");
const runtime = document.getElementById("runtime");
const resultsTable = document.getElementById("resultsTable");
const candidateDetails = document.getElementById("candidateDetails");
const message = document.getElementById("message");
const downloadBtn = document.getElementById("downloadBtn");

let candidates = [];


// ============================
// File Selection
// ============================

fileInput.addEventListener("change", function () {

    if (fileInput.files.length > 0) {

        message.textContent =
        "Selected File: " + fileInput.files[0].name;

    }

});

// ============================
// Populate Table
// ============================

function loadCandidates() {

    resultsTable.innerHTML = "";

    candidates.forEach(candidate => {

        const row = `
                    <tr>
                        <td>${candidate.rank}</td>
                        <td>${candidate.candidate_id}</td>
                        <td>${candidate.score}</td>
                        <td>
                            <button onclick="showCandidate(${candidate.rank - 1})">
                                View
                            </button>
                        </td>
                    </tr>
                    `;
        resultsTable.innerHTML += row;

    });

}

function showCandidate(index) {

    const candidate = candidates[index];

    candidateDetails.innerHTML = `
        <h3>${candidate.candidate_id}</h3>

        <p><strong>Rank:</strong> ${candidate.rank}</p>

        <p><strong>Final Score:</strong> ${candidate.score}</p>

        <p><strong>Explanation:</strong> ${candidate.reason}</p>
    `;
}
// ============================
// Start Ranking
// ============================

rankButton.addEventListener("click", async function () {

    if (fileInput.files.length === 0) {

        alert("Please select a candidate file first.");

        return;

    }

    status.textContent = "Processing...";

    runtime.textContent = "--";

    rankButton.disabled = true;

    rankButton.textContent = "Ranking...";

    const start = performance.now();

    const response = await fetch("/rank", {
        method: "POST"
    });

    candidates = await response.json();

    loadCandidates();

    const end = performance.now();

    runtime.textContent =
        ((end - start) / 1000).toFixed(2) + " sec";

    status.textContent = "Completed";

    rankButton.disabled = false;

    rankButton.textContent = "Start Ranking";

    message.textContent =
        "✔ Candidate ranking completed successfully!";
});

downloadBtn.addEventListener("click", function () {

    window.location.href = "/download";

});