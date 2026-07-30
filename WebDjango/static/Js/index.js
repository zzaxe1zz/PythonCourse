document.addEventListener("DOMContentLoaded", function () {
    if (!STRIPE_PUBLIC_KEY) {
        console.error("Error: STRIPE_PUBLIC_KEY no está definida.");
        return;
    }

    const stripe = Stripe(STRIPE_PUBLIC_KEY);

    const submitBtn = document.getElementById('submit');
    const clientsecret = submitBtn ? submitBtn.getAttribute('data-secret') : '';

    const options = {
        clientSecret: clientsecret,
        appearance: {
            theme: 'stripe',
        },
    };

    const elements = stripe.elements(options);
    const paymentElement = elements.create("payment");
    paymentElement.mount("#payment-element");

    const form = document.getElementById('payment-form');
    form.addEventListener('submit', function (ev) {
        ev.preventDefault();

        // Confirmar el SetupIntent para guardar la tarjeta
        stripe.confirmSetup({
            elements,
            confirmParams: {
                return_url: "http://127.0.0.1:8000/pagos/nuevo",
            },
        }).then(function (result) {
            if (result.error) {
                const displayError = document.getElementById('payment-message');
                displayError.textContent = result.error.message;
            }
        });
    });
});