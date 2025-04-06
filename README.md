# Linear Feedback Shift Registers
This repository contains multiple LFSR-based implementations in Python and Verilog, demonstrating applications in pseudo-random number generation (PRNG), stream ciphers, and hardware cryptography. <br />
<br />
📌 Features <br />
✅ LFSR in Python – Simulating LFSR behavior for PRNG. <br />
✅ LFSR-based PRNG in Verilog – FPGA-compatible pseudo-random number generator. <br />
✅ LFSR-based Stream Cipher – Encrypting data using LFSR-based keystream generation. <br />
<br />
1️⃣ LFSR in Python <br />
A simple 4-bit LFSR implementation using XOR feedback to generate a pseudo-random sequence. <br />
<br />
2️⃣ LFSR-based PRNG in Verilog <br />
A hardware compatible implementation of an LFSR-based pseudo-random number generator (PRNG) using Verilog for FPGA based applications.<br />
<br />
3️⃣ LFSR-based Stream Cipher <br />
An LFSR-based encryption system where LFSR output acts as a keystream for XOR-based encryption. <br />
Concept <br />
➤ LFSR generates a pseudo-random keystream. <br />
➤ XOR operation is used for stream cipher encryption/decryption. <br />
➤ Only sender and receiver need to know the LFSR parameters. <br />
<br />
📌 Applications <br />
➤ Random Number Generation (RNG) <br />
➤ Stream Ciphers & Encryption <br />
➤ Cryptographic Key Expansion <br />
➤ FPGA-based Secure Communication <br />
➤ Error Detection in Data Transmission <br />
