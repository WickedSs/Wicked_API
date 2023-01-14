import { faFileInvoice, faMoneyBill1Wave, faBoxesPacking, faShoppingBag, faGear, fa } from "@fortawesome/free-solid-svg-icons";


function getRandomNumberBetween(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function getRandomItemFromArray(array){
    return array[Math.floor(Math.random()*array.length)];
}

function UUID4() {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}

const formatter = (num) => {
    return parseFloat(num).toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,');
}

const parseJwt = (token) => {
    if (!token) { return; }
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace('-', '+').replace('_', '/');
    return JSON.parse(window.atob(base64));
}

const getCurrentDate = (separator='-') => {
    let newDate = new Date()
    let date = newDate.getDate();
    let month = newDate.getMonth() + 1;
    let year = newDate.getFullYear();
    
    return `${date < 10 ? `0${date}`: `${date}`}${separator}${month < 10 ? `0${month}`:`${month}`}${separator}${year}`
}

const tabs = [
    { index: 0, title: "Sellings", icon: faShoppingBag, scope: "Basic", role: "Admin, Employee" },
    { index: 1, title: "Products", icon: faBoxesPacking, scope: "Basic", role: "Admin, Employee" },
    { index: 2, title: "Expenses", icon: faMoneyBill1Wave, scope: "Basic", role: "Admin, Employee" },
    { index: 3, title: "Invoices", icon: faFileInvoice, scope: "Basic", role: "Admin, Employee" },
    { index: 4, title: "Settings", icon: faGear, scope: "Basic", role: "Admin" },
];
const registries = ["Someone", "Ben Cheikh AEK", "Ben Cheikh AER", "Ben Cheikh Hassane", "Ismain Azzaoui", "Mansouri Ali", "Nouar", "No Name"];

const invoice_base = {
    id: 0,
    operation_date: getCurrentDate("-"),
    buyer_name: "",
    buyer_address : "",
    invoice_number: 0,
    purchase_order: "",
    purchase_form: "",
    purchase_order_date: "",
    purchase_form_date: "",
    invoice_subtotal : 0,
    invoice_discount : 0,
    invoice_discount_price: 0,
    amount_paid: 0,
    amount_remaining: 0,
    invoice_tax : 0,
    invoice_tax_price : 0,
    invoice_total : 0,
    invoice_identifier: "",
    invoice_note: "",
    trade_registry: "",
    validation_deadline: "",
    is_validated: false,
    is_delivered: false,
}

const item_base = {
    id: 0,
    item_name: "",
    item_image: "default.png",
    item_price: undefined,
    item_quantity: undefined,
    item_barcode: undefined,
    is_manual: undefined,
    reference: "",
    item_size: "",
    item_model: ""
}

const product_base = {
    id: 0,
    product_name: undefined,
    category: undefined,
    model: undefined,
    barcode: undefined,
    quantity: undefined,
    imagePath: "default.png",
    price: undefined,
    identifier: undefined,
    sold: undefined,
    bought: undefined,
    market: undefined,
    earned: undefined,
    description: undefined,
    product_link: undefined,
    reference: undefined,
    colors: undefined,
    sizes: undefined,
    material_link: undefined,
    is_saved: undefined,
    is_active: undefined,
}

const constant = { formatter, getCurrentDate, registries, parseJwt, tabs, UUID4, invoice_base, item_base, product_base, getRandomNumberBetween, getRandomItemFromArray };
export default constant;