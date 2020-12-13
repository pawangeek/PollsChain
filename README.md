# PollsChain
A Decentralised digital Voting System based on Blockchain architecture.

## Inspiration
As we all know we need something to be more trusted since in the current US elections there are multiple allegations by Former President Donald Trump. So to smoothen the process I propose this blockchain-based voting system

## What it does
After vote casting there are six different steps are carried out for which we have designed a special REST API:
* Transaction Verification
* Proof of Work Algorithm
* Block creation and Serialization
* Block Broadcasting and validation
* Consensus Algorithm
* Byzantine Fault Tolerance

## Challenges I ran into
* It's really hard to set up that hash thing
* Another challenge is to create analysis in real-time
* Worked differently on both admin and voter submodules

## Accomplishments that I'm proud of
**That somehow able to manage to do so many things**

## Database Management:
* A relational DB SQLite is used as a database for the project.
* Many cryptographic and encryption algorithms are used to store the data securely in the database (SHA-256, CSPRNG, salt-hashing, etc).
* Complete normalization is also achieved in different relations of the database.

## Peer to Peer (Distributed) Network Design:
* A peer to peer distributed network on which the blockchain architecture works.
* A Web Socket request API for broadcasting the all the requests into P2P network.
* Handling concurrency by using a mutex lock mechanism.

## What's next for PollsChain
It can be implemented in the real-world easily by adding a module for Parties and Media House. But as I have to so in limited time, so it's really hard to do so many things in such a short span of time 
