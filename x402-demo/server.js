require("dotenv").config();

const express = require("express");

const {
    paymentMiddleware,
    x402ResourceServer
} = require("@x402/express");

const {
    HTTPFacilitatorClient
} = require("@x402/core/server");

const {
    ALGORAND_TESTNET_CAIP2
} = require("@x402/avm");


const app = express();


// --------------------------------------------------
// 1. Connect to the facilitator
// --------------------------------------------------

const facilitatorClient = new HTTPFacilitatorClient({
    url: process.env.FACILITATOR_URL
});


// --------------------------------------------------
// 2. Create x402 resource server
// --------------------------------------------------

const resourceServer = new x402ResourceServer(
    facilitatorClient
);


// --------------------------------------------------
// 3. Register Algorand payment scheme
// --------------------------------------------------

const { ExactAvmScheme } = require("@x402/avm/exact/server");

resourceServer.register(
    "algorand:*",
    new ExactAvmScheme()
);


// --------------------------------------------------
// 4. Define protected routes
// --------------------------------------------------

const routes = {

    "GET /register-pro": {

        accepts: {

            scheme: "exact",

            network: ALGORAND_TESTNET_CAIP2,

            payTo: process.env.RESOURCE_PAY_TO,

            price: "$0.01"

        },

        description:
            "Premium image registration using SAHM"

    }

};


// --------------------------------------------------
// 5. Enable x402 middleware
// --------------------------------------------------

app.use(
    paymentMiddleware(
        routes,
        resourceServer
    )
);


// --------------------------------------------------
// 6. Public endpoint
// --------------------------------------------------

app.get("/health", (req, res) => {

    res.json({
        status: "ok",
        service: "SAHM x402 Demo"
    });

});


// --------------------------------------------------
// 7. Protected premium endpoint
// --------------------------------------------------

app.get("/register-pro", (req, res) => {

    res.json({

        tier: "premium",

        algorithm: "SAHM",

        matches: 154,

        rmse: 0.89,

        status: "Registration Complete"

    });

});


// --------------------------------------------------
// 8. Start server
// --------------------------------------------------

const PORT = process.env.PORT || 4021;

app.listen(PORT, () => {

    console.log(
        `x402 server running at http://localhost:${PORT}`
    );

});