pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 10000;
    string customerName = "Jordan";
    string customerLastName = "Habib";
}

/*  
    * The `owner` variable: Holds the Ethereum address of the main customer (for example, 0xaaaaaaaaaaaaaaaaa).
    * The `isNewAccount` variable: Represents whether the account is new (that is, `true` or `false`).
    * The `accountBalance` variable: Holds the account balance (for example, 10000).
    * The `customerName` variable: Holds the first name of the customer (for example, "Jordan").
    * The `customerLastName` variable: Holds the last name of the customer (for example, "Habib").
*/