// script.js - Intelligent Scan Web UI Scripts

// Show toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('show');
    }, 100);

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 4000);
}

// Confirm before capturing face
function confirmCapture() {
    const confirmation = confirm("Do you want to start face capture?");
    if (confirmation) {
        window.location.href = "/capture";
    }
}

// Confirm before training
function confirmTrain() {
    const confirmation = confirm("Start training with captured data?");
    if (confirmation) {
        window.location.href = "/train";
    }
}

// Confirm recognition
function confirmRecognize() {
    const confirmation = confirm("Proceed with real-time face recognition?");
    if (confirmation) {
        window.location.href = "/recognize";
    }
}

// Inject toast CSS for dynamic use
const style = document.createElement("style");
style.textContent = `
.toast {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #1e88e5;
    color: #fff;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.3s ease;
    z-index: 1000;
}
.toast.show {
    opacity: 1;
    transform: translateY(0);
}
.toast.success { background: #43a047; }
.toast.error { background: #e53935; }
.toast.warning { background: #f9a825; }
`;
document.head.appendChild(style);
