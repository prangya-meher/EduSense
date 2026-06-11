import { api } from './api.js';

const alertBox = document.getElementById('alert-container');
const nextPage =
    new URLSearchParams(window.location.search).get('next');

function showMessage(container, message, isError = false) {
    container.innerHTML = `
        <div style="
            padding:10px;
            border-radius:8px;
            margin-bottom:10px;
            color:white;
            background:${isError ? '#e74c3c' : '#2ecc71'};
        ">
            ${message}
        </div>
    `;
}

document
    .getElementById('loginForm')
    .addEventListener('submit', async (e) => {

        e.preventDefault();

        const btn =
            document.getElementById('btn-login');

        const email =
            document.getElementById('email').value;

        const password =
            document.getElementById('password').value;

        btn.textContent = 'Logging in...';
        btn.disabled = true;

        try {

            const res =
                await api.login(email, password);

            if (res.success) {

                showMessage(
                    alertBox,
                    'Login successful!'
                );

                const session =
                    await api.me();

                if (session.success) {

                    const safeNextPage =
                        nextPage &&
                        /^[A-Za-z0-9._-]+\.html(?:\?.*)?$/.test(nextPage)
                            ? nextPage
                            : 'dashboard.html';

                    window.location.assign(
                        new URL(
                            safeNextPage,
                            window.location.href
                        ).href
                    );

                    return;
                }

                showMessage(
                    alertBox,
                    'Session verification failed.',
                    true
                );

            } else {

                showMessage(
                    alertBox,
                    res.error ||
                    'Invalid email or password.',
                    true
                );
            }

        } catch (error) {

            console.error(error);

            showMessage(
                alertBox,
                'Something went wrong.',
                true
            );

        } finally {

            btn.textContent = 'Login';
            btn.disabled = false;
        }
    });

const togglePassword =
    document.querySelector('.toggle-password');

const passwordInput =
    document.querySelector('#password');

if (togglePassword && passwordInput) {

    togglePassword.addEventListener(
        'click',
        () => {

            const type =
                passwordInput.getAttribute('type') === 'password'
                    ? 'text'
                    : 'password';

            passwordInput.setAttribute(
                'type',
                type
            );

            togglePassword.textContent =
                type === 'password'
                    ? '👁️'
                    : '🔒';
        }
    );
}

// function normalizeUser(response) {

//     if (!response.success || !response.data) {
//         return null;
//     }