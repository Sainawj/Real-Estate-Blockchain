// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RealEstate {
    struct Property {
        uint256 id;
        string name;
        string location;
        address owner;
        uint256 price;
        bool isAvailable;
    }

    uint256 public propertyCount;
    mapping(uint256 => Property) public properties;

    event PropertyListed(uint256 id, string name, string location, address owner, uint256 price);
    event PropertyPurchased(uint256 id, address newOwner);

    function listProperty(string memory _name, string memory _location, uint256 _price) public {
        propertyCount++;
        properties[propertyCount] = Property(propertyCount, _name, _location, msg.sender, _price, true);
        emit PropertyListed(propertyCount, _name, _location, msg.sender, _price);
    }

    function purchaseProperty(uint256 _id) public payable {
        Property storage property = properties[_id];
        require(property.isAvailable, "Property not available for sale");
        require(msg.value >= property.price, "Insufficient funds");

        property.owner = msg.sender;
        property.isAvailable = false;

        emit PropertyPurchased(_id, msg.sender);
    }

    function getProperty(uint256 _id) public view returns (Property memory) {
        return properties[_id];
    }
}