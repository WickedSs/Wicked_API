import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft, faL, faPlus } from "@fortawesome/free-solid-svg-icons";
import {createRef, useEffect, useRef, useState} from "react";
import API_CALLS from "../../app/api/api_routes";
import constant from "../../constants";

import default_png from '../../images/default.png'

function Input({ _ref, _element, _onKeyDown }) {
    return (
        <div className="vbox new_item_barcode">
            <input name="barcode" type="text" id={_element.id}
                placeholder={_element.placeholder}
                ref={_ref}
                value={_element.value}
                onChange={(e) => _updateValue(e.target.value, _element.index)}
                onKeyDown={(e) => _onKeyDown(e)}
            />
        </div>
    )
}

export default function NewItem({ _invoice, _currentInvoiceItems, _changed }) {
    const barcodeRef = createRef(), nameRef = createRef(), priceRef = createRef(), quantityRef = createRef();
    const { invoice, setInvoice } = _invoice;
    const { isChanged, setChanged } = _changed;
    const { currentInvoiceItems, setCurrentInvoiceItems } = _currentInvoiceItems;
    const [currentProduct, setCurrentProduct] = useState({});
    const [item, setItem] = useState({ barcode: undefined, name: undefined, price: undefined, quantity: undefined });

    useEffect(() => {
        _recalculate_invoice();
    }, [currentInvoiceItems])

    const _onFetch = async (e) => {
        if (e.key ==="Enter") {
            const response = item.barcode ? await API_CALLS.SELECT("product", "barcode", item.barcode, 3103) : undefined;
            if (response !== undefined && response?.status !== undefined) {
                setItem((prevState) => ({ 
                    name: response.data.product_name,
                    barcode: response.data.barcode,
                    price: response.data.item_price,
                }))
                setCurrentProduct(response.data);
                refs.current[3].focus();
            } else {
                let target = refs.current[0];
                if (target.className !== "error_select") {
                    target.className += "error_select";
                    setTimeout(() => target.className = "", 1200);
                }
            }
        }
    }
    
    const _recalculate_invoice = () => {
        const invoice_subtotal = currentInvoiceItems.reduce((accum, item) => {
            return accum + (item.item_quantity * item.item_price);
        }, 0);
        const invoice_tax_price = ((invoice.invoice_tax / 100) * invoice_subtotal);
        const invoice_total = invoice_subtotal + invoice_tax_price + (invoice.is_delivered ? 1500 : 0);
        setInvoice(prevState => ({
            ...prevState,
            invoice_subtotal : invoice_subtotal,
            invoice_tax_price: invoice_tax_price,
            invoice_total: invoice_total
        }));
    }

    const _submit_item = async (e) => {
        if (e.key === "Enter") {
            const new_item = {
                id: 0,
                item_name: item.name,
                item_price: item.price,
                item_quantity: item.quantity,
                item_identifier: invoice.invoice_identifier,
                is_manual: item.barcode !== undefined ? false : true,
                item_barcode: item.barcode || "",
                reference: currentProduct.reference || "", 
                item_size: currentProduct.colors || "", 
                item_model: currentProduct.sizes || "",
                item_image: currentProduct.imagePath || "default.png",
            };
            let response_invoiceItems = await API_CALLS.INSERT("invoiceItem", undefined, undefined, [new_item], 3102);
            if (response_invoiceItems?.status !== undefined) {
                setItem((prevState) => ({ ...prevState, barcode: undefined, name: undefined, price: undefined, quantity: undefined }));
                setCurrentInvoiceItems((prevState) => [...prevState, new_item]);
                setCurrentProduct({});
                setChanged(true);
            } else {
                console.log(response_invoiceItems);
            }
        }
    }

    return (
            <div className="new_invoice_item">
                <div className="inner_fields">
                    <div className="vbox new_item_barcode">
                        <input name="barcode" type="text"
                            placeholder="Enter Barcode" ref={barcodeRef} value={item.barcode || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, barcode: e.target.value }))}
                            onKeyDown={(e) => _onFetch(e)}
                        />
                    </div>
                    <div className="vbox new_item_name">
                        <input name="barcode" type="text"
                            placeholder="Enter Name" ref={nameRef} value={item.name || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, name: e.target.value }))}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && e.target.value.length > 0) {
                                    priceRef.current.focus();
                                }
                            }}
                        />
                    </div>
                    <div className="vbox new_item_price">
                        <input name="barcode" type="text"
                            placeholder="Enter Price" ref={priceRef} value={item.price || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, price: e.target.value }))}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && e.target.value.length > 0) {
                                    // priceRef.current.value = constant.formatter(item.price);
                                    quantityRef.current.focus();
                                }
                            }}
                        />
                    </div>
                    <div className="vbox new_item_quantity">
                        <input name="barcode" type="text"
                            placeholder="Enter Qte" ref={quantityRef} value={item.quantity || ""}
                            onChange={(e) => setItem((prevState) => ({ ...prevState, quantity: e.target.value }))}
                            onKeyDown={(e) => _submit_item(e)}
                        />
                    </div>
                </div>
            </div>
    )
}