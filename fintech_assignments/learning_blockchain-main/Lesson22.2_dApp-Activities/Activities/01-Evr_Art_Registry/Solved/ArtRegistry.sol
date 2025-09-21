pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") {}

    // Create artwork struct with a name, artist, & appraisalValue
    struct Artwork {
        string name;
        string artist;
        uint256 appraisalValue;
    }

    // Create a dictionary-like mapping of Artwork struct using uint256 as key
    mapping(uint256 => Artwork) public artCollection;

    // Set up an event log to avoid expensive, on-chain data storage
    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI);

    // Create registerArtwork function & return the tokenId
    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Set mapping artCollection to the Artwork struct
        artCollection[tokenId] = Artwork(name, artist, initialAppraisalValue);

        return tokenId;
    }

    // Create newAppraisal function that can change the appraisal value 
    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {

        // Set newAppraisal value to artCollection using tokenId
        artCollection[tokenId].appraisalValue = newAppraisalValue;

        // Fire off the event Appraisal using emit
        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        // Return updated artCollection
        return artCollection[tokenId].appraisalValue;
    }
}
