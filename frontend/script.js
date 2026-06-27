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

// ============================
// Sample Candidates
// ============================

const candidates = [
    {
        rank: 1,
        id: "CAND_000123",
        score: 95.6,
        role: "Senior AI Engineer",
        experience: "7 Years",
        behavior: 88,
        consistency: 94,
        skills: "Python, LLM, RAG, Pinecone, FAISS",
        explanation: "Excellent match with AI engineering role. Strong technical skills and recruiter engagement."
    },
    {
        rank: 2,
        id: "CAND_000456",
        score: 93.2,
        role: "Machine Learning Engineer",
        experience: "6 Years",
        behavior: 82,
        consistency: 91,
        skills: "Python, TensorFlow, Retrieval, Qdrant",
        explanation: "Strong AI profile with consistent career progression."
    },
    {
        rank: 3,
        id: "CAND_000789",
        score: 91.8,
        role: "Data Scientist",
        experience: "5 Years",
        behavior: 79,
        consistency: 89,
        skills: "Python, ML, NLP, Embeddings",
        explanation: "Good AI skills and recruiter engagement."
    }
];
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
                <td>${candidate.id}</td>
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
        <h3>${candidate.id}</h3>

        <p><strong>Role:</strong> ${candidate.role}</p>

        <p><strong>Experience:</strong> ${candidate.experience}</p>

        <p><strong>Skills:</strong> ${candidate.skills}</p>

        <p><strong>Behavior Score:</strong> ${candidate.behavior}</p>

        <p><strong>Consistency Score:</strong> ${candidate.consistency}</p>

        <p><strong>Final Score:</strong> ${candidate.score}</p>

        <p><strong>Explanation:</strong> ${candidate.explanation}</p>
    `;
}

// ============================
// Start Ranking
// ============================

rankButton.addEventListener("click", function () {

    if (fileInput.files.length === 0) {

        alert("Please select a candidate file first.");

        return;

    }

    status.textContent = "Processing...";

    runtime.textContent = "--";

    rankButton.disabled = true;

    rankButton.textContent = "Ranking...";

    setTimeout(function () {

        status.textContent = "Completed";
        status.className = "completed";

        runtime.textContent = "39 sec";

        rankButton.disabled = false;

        rankButton.textContent = "Start Ranking";

        loadCandidates();

        message.textContent =
    "✔ Candidate ranking completed successfully!";

    }, 3000);

});