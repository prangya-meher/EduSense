import { api } from "./api.js";

async function initDashboard() {

    const res = await api.me();


    if (!res.success || !res.data) {
        window.location.href = "login.html";
        return;
    }

    const user = res.data;

    const fullName =
        user.full_name ||
        `${user.first_name || ""} ${user.last_name || ""}`.trim() ||
        user.email.split("@")[0];

    const firstName = fullName.split(" ")[0];

    document.getElementById("welcome-title").textContent =
        `Welcome back, ${firstName}! 👋`;

    document.getElementById("user-name-header").textContent =
        fullName;

    document.getElementById("profile-initials").textContent =
        firstName.charAt(0).toUpperCase();

    document.getElementById("auth-content").style.display =
        "grid";

    if (user.is_superuser) {
        const adminMenu =
            document.getElementById("admin-menu");

        if (adminMenu) {
            adminMenu.style.display = "block";
        }
    }
}

async function handleLogout(event) {
    event.preventDefault();

    await api.logout();
    window.location.href = "index.html";
}

const logoutBtn =
    document.getElementById("logout-btn");

if (logoutBtn) {
    logoutBtn.addEventListener(
        "click",
        handleLogout
    );
}

const dashboardHamburger =
    document.getElementById(
        "dashboard-hamburger"
    );

const sidebar =
    document.getElementById("sidebar");

if (dashboardHamburger) {
    dashboardHamburger.addEventListener(
        "click",
        () => {
            sidebar.classList.toggle("active");
        }
    );
}

document.addEventListener("click", (e) => {
    if (
        window.innerWidth <= 900 &&
        sidebar &&
        dashboardHamburger
    ) {
        if (
            !sidebar.contains(e.target) &&
            !dashboardHamburger.contains(e.target)
        ) {
            sidebar.classList.remove("active");
        }
    }
});

initDashboard();