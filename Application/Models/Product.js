

export default class Product {


    constructor(productName, model, barcode, quantity, imagePath, price, identifier, dimentions, sold, bought, market, earned, description, link, reference, availableColors, availableSizes, materialLink, isActive) {
        this.productName = productName;
        this.model = model;
        this.barcode = barcode;
        this.quantity = quantity;
        this.imagePath = imagePath;
        this.price = price;
        this.identifier = identifier;
        this.dimentions = dimentions;
        this.sold = sold;
        this.bought = bought;
        this.market = market;
        this.earned = earned;
        this.description = description;
        this.link = link;
        this.reference = reference;
        this.availableColors = availableColors;
        this.availableSizes = availableSizes;
        this.materialLink = materialLink;
        this.isActive = isActive;
        this.currentQuantity = 1;
        this.isSaved = false;
    }

    set setCurrentQuantity(value) {
        this.currentQuantity + value;
    }

};