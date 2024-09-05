# Real Estate Management using Blockchain Smart-Contract

## MVP Specification
The Minimum Viable Product (MVP) for the "Real Estate Management using Blockchain Smart-Contract" focuses on creating a decentralized platform that enables secure, transparent, and immutable real estate transactions. The MVP include basic functionalities for property listing, buyer-seller agreements via smart contracts, and storage of property records on a distributed database.
## Core Features:
> User Registration and Authentication

> Property Listing Management

> Smart Contract Deployment for Transactions

> Immutable Record Storage

> User Dashboard

> Transaction History

## Architecture
Architecture Overview:
The architecture for the MVP consists of three primary layers:
## Frontend:
> React: Handles user interactions and sends requests to the backend.

> CSS/Bootstrap: Provides styling for the user interface.

## Backend:
> Flask/Django (Python): Manages API requests, handles business logic, and interacts with the blockchain.

> Web3.py: Facilitates communication between the backend and the Ethereum blockchain.

## Blockchain and Storage:
> Ethereum (Solidity): Manages smart contracts and transaction records.

> IPFS (InterPlanetary File System): Stores immutable property records.

> MongoDB: Stores non-critical data and user information.

## Data Flow:
> User Interacts with Frontend (React): User requests (e.g., register, list a property) are sent to the backend.

> Backend Processes Request (Flask/Django): The backend processes the request, performs necessary business logic, and interacts with the blockchain using Web3.py.

> Smart Contract Execution (Ethereum): Smart contracts are deployed/executed on the Ethereum blockchain.

> Record Storage (IPFS/MongoDB): Immutable records are stored in IPFS, while user data and non-critical information are stored in MongoDB.

> Response to Frontend: The backend returns the outcome to the frontend, updating the user interface accordingly.

# APIs and Methods
> API Routes:
>> /api/users

> POST: Register a new user.

> GET: Retrieve user profile information.
/api/auth

> POST: Authenticate user credentials and issue a token.
/api/properties

> GET: Fetch the list of available properties.

> POST: Add a new property to the listing.
/api/contracts

> POST: Deploy a new smart contract for a transaction.

> GET: Retrieve transaction history for a specific user.
/api/transactions

> GET: Fetch details of a specific transaction.

> POST: Initiate a new transaction (e.g., buying a property).

## API Endpoints/Methods:
class Web3.eth.Contract(address=None, abi=None)
Contract(address): Instantiate a contract object by specifying its address on the blockchain.
call(args): Calls a method of the contract with provided arguments, without sending a transaction.
sendTransaction(args): Sends a transaction to a contract method, modifying the blockchain state.

## 3rd Party APIs:
Infura API:
POST /v3/PROJECT-ID: Interact with the Ethereum blockchain without running your own node.
IPFS API:
POST /api/v0/add: Add a file or data to IPFS.
GET /api/v0/cat: Retrieve data from IPFS using its hash.







