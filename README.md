# Real Estate Management using Blockchain Smart-Contract
A decentralized system for real estate transactions. Features user authentication, property management, and smart contracts. Built with React, Flask/Django, Ethereum, IPFS, and MongoDB. Includes Docker setups for both frontend and backend

The MVP include basic functionalities for property listing, buyer-seller agreements via smart contracts, and storage of property records on a distributed database.
## Core Features:
>> User Registration and Authentication
>> Property Listing Management
>> Smart Contract Deployment for Transactions
>> Immutable Record Storage
>> User Dashboard
>> Transaction History

## Architecture Overview:
The architecture for the MVP consists of three primary layers:
## Frontend:
React: Handles user interactions and sends requests to the backend.
CSS/Bootstrap: Provides styling for the user interface.
## Backend:
> Flask/Django (Python): Manages API requests, handles business logic, and interacts with the blockchain.
> Web3.py: Facilitates communication between the backend and the Ethereum blockchain.
> Blockchain and Storage:
> Ethereum (Solidity): Manages smart contracts and transaction records.
> IPFS (InterPlanetary File System): Stores immutable property records.
> MongoDB: Stores non-critical data and user information.

## Data Flow:
> User Interacts with Frontend (React): User requests (e.g., register, list a property) are sent to the backend.
> Backend Processes Request (Flask/Django): The backend processes the request, performs necessary business logic, and interacts with the blockchain using Web3.py.
> Smart Contract Execution (Ethereum): Smart contracts are deployed/executed on the Ethereum blockchain.
> Record Storage (IPFS/MongoDB): Immutable records are stored in IPFS, while user data and non-critical information are stored in MongoDB.
> Response to Frontend: The backend returns the outcome to the frontend, updating the user interface accordingly.
