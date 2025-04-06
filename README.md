# Linear Feedback Shift Registers
This repository contains multiple LFSR-based implementations in Python and Verilog, demonstrating applications in pseudo-random number generation (PRNG), stream ciphers, and hardware cryptography.

📌 Features
✅ LFSR in Python – Simulating LFSR behavior for PRNG.
✅ LFSR-based PRNG in Verilog – FPGA-compatible pseudo-random number generator.
✅ LFSR-based Stream Cipher – Encrypting data using LFSR-based keystream generation.

1️⃣ LFSR in Python
A simple 4-bit LFSR implementation using XOR feedback to generate a pseudo-random sequence.

2️⃣ LFSR-based PRNG in Verilog
A hardware compatible implementation of an LFSR-based pseudo-random number generator (PRNG) using Verilog for FPGA based applications.

3️⃣ LFSR-based Stream Cipher
An LFSR-based encryption system where LFSR output acts as a keystream for XOR-based encryption.
Concept
➤ LFSR generates a pseudo-random keystream.
➤ XOR operation is used for stream cipher encryption/decryption.
➤ Only sender and receiver need to know the LFSR parameters.

📌 Applications
➤ Random Number Generation (RNG)
➤ Stream Ciphers & Encryption
➤ Cryptographic Key Expansion
➤ FPGA-based Secure Communication
➤ Error Detection in Data Transmission
