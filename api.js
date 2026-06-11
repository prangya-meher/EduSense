const API_HOST = window.location.hostname || "127.0.0.1";
const BASE_URL = `http://${API_HOST}:8000/api`;

function getErrorMessage(data) {
    if (!data) return "Request failed";

    if (typeof data.error === "string") {
        return data.error;
    }

    if (data.error && typeof data.error === "object") {
        return Object.values(data.error).flat().join(", ");
    }

    return "Request failed";
}

function normalizeUser(response) {
    if (!response || response.success === false) {
        return null;
    }

    return response.user || response.data || response;
}

async function fetchAPI(endpoint, options = {}) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            ...options,
        });

        const data = await response.json();

        return {
    success: response.ok,
    data: data,
    error: response.ok ? null : getErrorMessage(data),
};

    } catch (error) {
        console.error(error);

        return {
            success: false,
            error: "Unable to connect to server",
        };
    }
}

const api = {

    register(firstName, lastName, email, password, confirmPassword) {
        return fetchAPI("/auth/register/", {
            method: "POST",
            body: JSON.stringify({
                first_name: firstName,
                last_name: lastName,
                email,
                password,
                confirm_password: confirmPassword,
            }),
        });
    },

    verifyOTP(email, otp) {
        return fetchAPI("/auth/verify-otp/", {
            method: "POST",
            body: JSON.stringify({
                email,
                otp,
            }),
        });
    },

    async login(email, password) {
        const response = await fetchAPI("/auth/login/", {
            method: "POST",
            body: JSON.stringify({
                email,
                password,
            }),
        });

        const user = normalizeUser(response);

        if (response.success && user) {
            localStorage.setItem(
                "edusenseUser",
                JSON.stringify(user)
            );
        }

        return response;
    },

    async me() {
        const response = await fetchAPI("/auth/me/", {
            method: "GET",
        });

        const user = normalizeUser(response);

        if (user) {
            localStorage.setItem(
                "edusenseUser",
                JSON.stringify(user)
            );
        }

        return {
            success: Boolean(user),
            data: user,
        };
    },

    async logout() {
        localStorage.removeItem("edusenseUser");

        return fetchAPI("/auth/logout/", {
            method: "POST",
        });
    },

    getCachedUser() {
        try {
            return JSON.parse(
                localStorage.getItem("edusenseUser")
            );
        } catch {
            return null;
        }
    },
    async requireAuth() {
    const response = await this.me();

    if (!response.success) {
        window.location.href = "login.html";
        return null;
    }

    return response.data;
}
};

export { api,fetchAPI  };
window.api = api;
window.fetchAPI = fetchAPI;