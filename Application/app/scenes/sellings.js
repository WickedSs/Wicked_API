import { createRef, useEffect, useState } from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronUp, faChevronDown } from "@fortawesome/free-solid-svg-icons";


import '../../styles/sellings.css';
import constant from '../../constants';
import API_CALLS from '../api/api_routes';
import PanierItem from '../../components/Sellings/panier_item';


function EmptyPanier() {
    return (
        <div className='empty_panier'>
            Empty!
        </div>
    )
}


export default function Sellings({ _currentTradeRegistry }) {

    const barcodeRef = createRef(), nameRef = createRef(), priceRef = createRef(), quantityRef = createRef();
    const [error, setError] = useState(false);
    const [item, setItem] = useState({ barcode: undefined, name: undefined, price: undefined, quantity: undefined })
    const [currentProduct, setCurrentProduct] = useState({});
    const [panier, setPanier] = useState([]);
    const [invoice, setInvoice] = useState(constant.invoice_base);

    useEffect(() => {
        const _registry_change = () => {
            setInvoice(prevState => ({ ...prevState, 
                trade_registry: constant.registries[_currentTradeRegistry],
                invoice_identifier: constant.UUID4().split("-").pop(),
            }))
        }
        _registry_change();
    }, [_currentTradeRegistry]);

    useEffect(() => {
        const _new_item = () => {
            let invoice_subtotal = panier.reduce((accumelator, value) => {
                return accumelator + (value.price * value.currentQuantity);
            }, 0);
            let invoice_tax_price = ((invoice.invoice_tax / 100) * invoice.invoice_subtotal);
            let invoice_total = invoice_subtotal + invoice_tax_price + (invoice.is_delivered ? 1500 : 0);
            setInvoice(prevState => ({ ...prevState, invoice_subtotal : invoice_subtotal, invoice_tax_price: invoice_tax_price, invoice_total: invoice_total }));
        }
        _new_item();
    }, [panier]);

    const _remove_item_from_panier = (id) => setPanier(panier.filter(item => item.id != id));
    
    const _alter_quantity = (id, value) => {
        let _panier_copy = [...panier];
        let working_item = _panier_copy.filter(item => item.id == id)[0];
        working_item.currentQuantity = working_item.currentQuantity + value;
        if (working_item.currentQuantity > working_item.quantity) {
            working_item.currentQuantity = working_item.quantity
        } else if (working_item.currentQuantity <= 1) {
            working_item.currentQuantity = 1;
        }
        setPanier(_panier_copy);
    }

    const _alter_color = (id, value) => {
        let _panier_copy = [...panier];
        let working_item = _panier_copy.filter(item => item.id === id)[0];
        let index = working_item.colors.indexOf(working_item.currentColor);
        index += 1;
        if (index >= working_item.colors.length) { index = 0; }
        working_item.currentColor = working_item.colors[index];
        setPanier(_panier_copy);
    }

    const _alter_size = (id, value) => {
        let _panier_copy = [...panier];
        let working_item = _panier_copy.filter(item => item.id === id)[0];
        let index = working_item.colors.indexOf(working_item.currentSize);
        index += 1;
        if (index >= working_item.sizes.length) { index = 0; }
        working_item.currentSize = working_item.sizes[index];;
        setPanier(_panier_copy);
    }

    const _pick_item = async (e) => {
        if (e.key == "Enter") {
            let response = await API_CALLS.SELECT("product", "barcode", item.barcode, 3103);
            if (response?.status !== undefined) {
                setCurrentProduct(response.data);
                setItem((prevState) => ({ ...prevState, name: response.data.product_name, price: response.data.price }));
                quantityRef.current.focus();
            } else {
                let target = barcodeRef.current;
                if (target.className !== "error_select") {
                    target.className += "error_select";
                    setTimeout(() => target.className = "", 1200);
                }
            }
        }
    }

    const _add_item_to_panier = (e) => {
        if (e.key === "Enter" && item.quantity > 0) {
            const exist = panier.find(element => element.id == currentProduct.id);
            if (exist != undefined) {
                setError(true);
                return -1;
            }
            currentProduct.product_name = item.name;
            currentProduct.price = item.price;
            currentProduct.quantity = item.barcode ? currentProduct.quantity : 9999;
            currentProduct.currentQuantity = parseInt(item.quantity);
            currentProduct.is_manual = item.barcode ? false : true;
            currentProduct.item_model = currentProduct.colors || "";
            currentProduct.item_size = currentProduct.sizes || "";
            barcodeRef.current.focus();
            setPanier((prevState) => [...prevState, currentProduct]);
            _clean();
        }
    }

    const _append_quantity = () => {
        const working_item = panier.find(element => element.barcode == currentProduct.barcode);
        _alter_quantity(working_item.id, parseInt(item.quantity));
        _clean();
    }

    const _cancel_quantity = () => _clean();

    const _clean = () => {
        setError(false); 
        setCurrentProduct({});
        setItem((prevState) => ({ ...prevState, barcode: undefined, name: undefined, price: undefined, quantity: undefined }));
    }

    const _submit_invoice = async () => {
        if (panier.length > 0 && invoice.buyer_name && invoice.buyer_address) {
            let response_invoice = await API_CALLS.INSERT("invoice", undefined, undefined, invoice, 3101);
            if (response_invoice?.status !== undefined) {
                let invoice_items = [];
                panier.map((item, index) => {
                    invoice_items.push({
                        id: 0,
                        item_name: item.product_name,
                        item_image: item.barcode ? item.imagePath : "default.png",
                        item_price: item.price,
                        item_quantity: item.currentQuantity,
                        item_identifier: invoice.invoice_identifier,
                        item_barcode: item.barcode || "",
                        is_manual: item.barcode ? false : true,
                        reference: item.reference || "",
                        item_size: item.currentSize || "",
                        item_model: item.currentColor || ""
                    });
                })
                let response_invoiceItems = await API_CALLS.INSERT("invoiceItem", undefined, undefined, invoice_items, 3102);
                if (response_invoiceItems?.status !== undefined) {
                    setPanier([]);
                    setInvoice(constant.invoice_base);
                }
            }
        }
    }


    return (
        <div className='selling_scene'>
            <div className='selling_left_side'>
                <div className="top_area">
                    <div className="vbox product_barcode">
                        <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Barcode</label>
                        <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Barcode" ref={barcodeRef} value={item.barcode || ""}
                            onChange={(e) => setItem((prevState) => ({
                                ...prevState, barcode: e.target.value
                            }))}
                            onKeyDown={(e) => _pick_item(e)}
                        />
                    </div>
                    <div className="vbox product_name">
                        <label htmlFor="nameInput" style={{ marginBottom: 5 }}>Name</label>
                        <input name="name" type="text" id="nameInput" placeholder="Enter Name" ref={nameRef} value={item.name || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, name: e.target.value }))}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && e.target.value.length > 0) {
                                    priceRef.current.focus();
                                }
                            }}
                        />
                    </div>
                    <div className="vbox product_price">
                        <label htmlFor="priceInput" style={{ marginBottom: 5 }}>Price</label>
                        <input name="price" type="text" id="priceInput" placeholder="Enter Price" ref={priceRef} value={item.price ? constant.formatter(item.price) : ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, price: e.target.value }))}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && e.target.value.length > 0) {
                                    quantityRef.current.focus();
                                }
                            }}
                        />
                    </div>
                    <div className="vbox product_quantity">
                        <label htmlFor="quantityInput" style={{ marginBottom: 5 }}>Quantity</label>
                        <input name="quantity" type="text" id="quantityInput" placeholder="Enter Qte" ref={quantityRef} value={item.quantity || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, quantity: e.target.value }))}
                            onKeyDown={(e) => _add_item_to_panier(e)}
                        />
                    </div>
                </div>
                <div className={'error_area ' + (error ? "active_error" : "")}>
                    <div className='error_message'>This item already exist in your basket</div>
                    <div className='action_buttons'>
                        <button onClick={() => _cancel_quantity()}>Cancel</button>
                        <button onClick={() => _append_quantity()}>Quantity</button>
                    </div>
                </div>
                <div className='middle_area' style={{ justifyContent: panier.length > 0 ? "flex-start" : "center" }}>
                    {panier.length <= 0 && (<EmptyPanier />) }
                    {panier.length > 0 && panier.map((item, index) =>
                            <PanierItem key={index} item={item}
                                _onDelete={_remove_item_from_panier}
                                _onAlterQuantity={_alter_quantity}
                                _onAlterColor={_alter_color}
                                _onAlterSize={_alter_size}
                            />
                        )
                    }
                </div>
            </div>
            <div className='selling_right_side'>
                <div className='delivery_tax' style={{ marginTop: 0 }}>
                    <div className='vbox delivery_options'>
                        <label htmlFor="buyerInput">Delivery</label>
                        <div className='selection'
                            onClick={() => setInvoice(prevState => ({
                                ...prevState, 
                                is_delivered : !invoice.is_delivered,
                                invoice_total: invoice.is_delivered ? (invoice.invoice_total - 1500) : (invoice.invoice_total + 1500)
                            }))}>
                            <div className='selected'>{invoice.is_delivered ? "Yes" : "No"}</div>
                            <div className='chevrons'>
                                <FontAwesomeIcon icon={faChevronUp} style={{ fontSize: 10, color: "#fff" }} />
                                <FontAwesomeIcon icon={faChevronDown} style={{ fontSize: 10, color: "#fff" }} />
                            </div>
                        </div>
                    </div>
                    <div className='vbox tax_options'>
                        <label htmlFor="buyerInput">Tax</label>
                        <div className='selection'
                            onClick={() => setInvoice(prevState => ({
                                ...prevState,
                                invoice_tax : invoice.invoice_tax == 0 ? 19 : 0,
                                invoice_tax_price: (((invoice.invoice_tax == 0 ? 19 : 0) / 100) * (invoice.invoice_subtotal)),
                                invoice_total: invoice.invoice_subtotal + (((invoice.invoice_tax == 0 ? 19 : 0) / 100) * invoice.invoice_subtotal) + (invoice.is_delivered ? 1500 : 0)
                            }))}>
                            <div className='selected'>{invoice.invoice_tax}%</div>
                            <div className='chevrons'>
                                <FontAwesomeIcon icon={faChevronUp} style={{ fontSize: 10, color: "#fff" }} />
                                <FontAwesomeIcon icon={faChevronDown} style={{ fontSize: 10, color: "#fff" }} />
                            </div>
                        </div>
                    </div>
                </div>
                <div className="buyer_details">
                    <div className="vbox invoice_buyer">
                        <label htmlFor="buyerInput">Buyer Name</label>
                        <input name="buyer" type="text" id="buyerInput" placeholder="Enter buyer name"
                            onChange={(e) => setInvoice(prevState => ({ ...prevState, buyer_name : e.target.value }))}
                            value={invoice.buyer_name}
                        />
                    </div>
                    <div className="vbox buyer_address">
                        <label htmlFor="addressInput">Buyer Address</label>
                        <input name="address" type="text" id="addressInput" placeholder="Enter buyer address"
                            onChange={(e) => setInvoice(prevState => ({ ...prevState, buyer_address : e.target.value }))}
                            value={invoice.buyer_address}
                        />
                    </div>
                </div>
                <div className='vbox invoice_detail'>
                    <div className='line subtotal'>
                        <div>Operation Date</div>
                        <div>{invoice.operation_date}</div>
                    </div>
                    <div className='line subtotal'>
                        <div>Subtotal</div>
                        <div>{constant.formatter(invoice.invoice_subtotal)}</div>
                    </div>
                    <div className='line discount'>
                        <div>Discount</div>
                        <div>({invoice.invoice_discount}%) - {constant.formatter(invoice.invoice_discount_price)}</div>
                    </div>
                    <div className='line delivery'>
                        <div>Delivery</div>
                        <div>{invoice.is_delivered ? "1500.00" : "0.00"}</div>
                    </div>
                    <div className='line tax'>
                        <div>Tax</div>
                        <div>({invoice.invoice_tax}%) - {constant.formatter(invoice.invoice_tax_price)}</div>
                    </div>
                    <div className='line total'>
                        <div>Total</div>
                        <div>{constant.formatter(invoice.invoice_total)}</div>
                    </div>
                </div>
                <div className="vbox buyer_paid_deadline">
                    <div className='buyer_paid'>
                        <label htmlFor="paidInput">Amount Paid?</label>
                        <input name="paid" type="text" id="paidInput" placeholder="Enter Amount Paid"
                            onChange={(e) => setInvoice(prevState => ({ ...prevState, amount_paid : e.target.value }))}
                            value={constant.formatter(invoice.amount_paid)}
                        />
                    </div>
                    <div className='buyer_deadline'>
                        <label htmlFor="deadlineInput">Deadline</label>
                        <input name="deadline" type="text" id="deadlineInput" placeholder="DD-MM-YYYY"
                            onChange={(e) => setInvoice(prevState => ({ ...prevState, validation_deadline : e.target.value }))}
                            value={invoice.validation_deadline}
                        />
                    </div>
                </div>
                <div className='vbox total'>
                    <div className='button submit'>
                        <button onClick={() => _submit_invoice()}>Proceed to checkout</button>
                        <button>Continue shopping</button>
                    </div>
                </div>
            </div>
        </div>
    )
}