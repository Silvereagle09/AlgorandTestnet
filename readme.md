## Project Overview

This project is a Scale-Adaptive Image Registration System designed to handle image pairs with varying levels of complexity.

The system follows a tiered-access model:

### Basic Version

The basic version is intended for image pairs that are relatively easy to register, such as:

- Low scale differences
- Minimal viewpoint changes
- Limited illumination variation
- Simple geometric transformations

These images can be processed using lightweight and computationally efficient feature matching techniques, allowing users to obtain results without additional cost.

### Premium Version

The premium version is designed for challenging image registration scenarios involving:

- Large scale differences
- Significant viewpoint variations
- Illumination changes
- Geometric distortions
- Multi-condition image matching

These cases require advanced registration algorithms and significantly higher computational resources.

To access premium processing, users make a payment through the Algorand blockchain. Once the payment is verified, premium features are unlocked and the image pair is processed using the advanced registration pipeline.

---

## Why Algorand?

Algorand is used as the payment and access-control layer of the platform.

### Payment Flow

User
→ Requests Premium Processing
→ Makes Payment using Algorand
→ Transaction is Verified
→ Premium Features are Unlocked
→ Advanced Registration Pipeline Executes

Benefits of using Algorand:

- Fast transaction finality
- Low transaction fees
- Transparent payment verification
- Secure access control
- Scalable payment infrastructure

---

## Monetization Model

| Version | Features | Access |
|----------|----------|---------|
| Basic | Standard image registration for simple image pairs | Free |
| Premium | Advanced registration for complex image pairs with large variations | Paid via Algorand |
