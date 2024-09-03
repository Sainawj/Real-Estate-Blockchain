pragma solidity ^0.8.0;

contract PropertyContract {
    struct Property {
        uint id;
        string title;
        string description;
        uint price;
        address owner;
    }

    mapping(uint => Property) public properties;
    uint public propertyCount;

    event PropertyListed(uint id, string title, address owner);
    event PropertySold(uint id, address newOwner);

    function listProperty(string memory _title, string memory _description, uint _price) public {
        propertyCount++;
        properties[propertyCount] = Property(propertyCount, _title, _description, _price, msg.sender);
        emit PropertyListed(propertyCount, _title, msg.sender);
    }

    function buyProperty(uint _id) public payable {
        Property storage property = properties[_id];
        require(msg.value >= property.price, "Not enough funds sent");
        require(property.owner != address(0), "Property not found");

        address payable seller = payable(property.owner);
        property.owner = msg.sender;
        seller.transfer(msg.value);

        emit PropertySold(_id, msg.sender);
    }
}