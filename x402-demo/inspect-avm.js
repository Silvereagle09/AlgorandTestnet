// inspect-avm.js
const { ExactAvmScheme } = require("@x402/avm/exact/server");

console.log(
    Object.getOwnPropertyNames(ExactAvmScheme.prototype)
);