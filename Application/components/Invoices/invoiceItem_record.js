import Image from 'next/image'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMinus, faTrash, faPlus, faArrowsUpDown } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";

import constant from "../../constants"
import API_CALLS from "../../app/api/api_routes";
import default_png from '../../images/default.png'

export default function InvoiceItemRecord({ _invoiceState, _item, _invoiceItems, _changed }) {

    const [respectiveProduct, setRespectiveProduct] = useState({});
    const { invoice, setInvoice } = _invoiceState;
    const { currentInvoiceItems, setCurrentInvoiceItems } = _invoiceItems;
    const { isChanged, setChanged } = _changed;

    useEffect(() => {
        const fetch_product = async () => {
            if (!_item.is_manual) {
                const response = await API_CALLS.SELECT("product", "barcode", _item.item_barcode, 3103);
                setRespectiveProduct(response.data);
            }
        }
        fetch_product();
    }, []);

    useEffect(() => {
        _recalculate_invoice();
    }, [currentInvoiceItems])

    const _onAlterSize = (id) => {

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

    const _onAlterQuantity = (id, value) => {
        let _items_copy = [...currentInvoiceItems];
        let working_item = _items_copy.filter(item => item.id == id)[0];
        working_item.item_quantity = working_item.item_quantity + value;
        if (working_item.item_quantity > respectiveProduct.quantity && !_item.is_manual) {
            working_item.item_quantity = respectiveProduct.quantity
        }
        setCurrentInvoiceItems(_items_copy);
        setChanged(true);
    }

    const _onDelete = async (id) => {
        let delete_response = await API_CALLS.DELETE("invoiceItem_id", undefined, _item.id, 3102);
        if (delete_response?.status) {
            let items_temp = [...currentInvoiceItems];
            items_temp = items_temp.filter(item => item.id != id);
            setCurrentInvoiceItems(items_temp);
        } else {
            console.log(delete_response);
        }
    }

    return (
        <div className="panier_item">
            <div className='panier_image'>
                <Image src={default_png} width={128} height={128} objectFit='fit' />
            </div>
            <div className="panier_infos">
                <div className='item_name'>
                    <div>
                        {_item.item_name}
                    </div>
                    <div>
                        {constant.formatter(_item.item_price * _item.item_quantity)}
                    </div>
                </div>
                <div className='item_price'>
                    <div>
                        {constant.formatter(_item.item_price)}
                    </div>
                    <div style={{ color: _item.is_manual ? "#f6bd60" : respectiveProduct.quantity > 0 ? "#2a9d8f" : "#ff595e" }}>
                        { _item.is_manual ? "Manual" : respectiveProduct.quantity > 0 ? "In Stock" : "Out Of Stock"}
                    </div>
                </div>
                <div className='item_size_stock_quantity'>
                    <div className='item_left_side'>
                        {
                            _item.item_size && (
                            <div className='show size' onClick={() => _onAlterSize(_item.id)}>
                                <div className='field'>
                                    <div className='selected'>{_item.item_size}</div>
                                    {/* <FontAwesomeIcon icon={faArrowsUpDown} style={{ fontSize: 16, color: "#fff" }} /> */}
                                </div>
                            </div> )
                        }
                        {
                            _item.item_model && (
                                <div className='show color' onClick={() => _onAlterColor(_item.id)}>
                                    <div className='field'>
                                        <div className='selected'>{_item.item_model}</div>
                                        {/* <FontAwesomeIcon icon={faArrowsUpDown} style={{ fontSize: 16, color: "#fff" }} /> */}
                                    </div>
                                </div>
                            )
                        }
                        <div className='show quantity'>
                            <div onClick={() => _onAlterQuantity(_item.id, -1) }>
                                <FontAwesomeIcon icon={faMinus} style={{ fontSize: 16, color: "#fff" }} />
                            </div>
                            <div className='selected' contentEditable="true" suppressContentEditableWarning={true} style={{ textAlign: 'center' }}>
                                { _item.item_quantity }
                            </div>
                            <div onClick={() => _onAlterQuantity(_item.id, 1) }>
                                <FontAwesomeIcon icon={faPlus} style={{ fontSize: 16, color: "#fff" }} />
                            </div>
                        </div>
                    </div>
                    <div className='item_right_side'>
                        {/* <div className='icon_button favourite' onClick={() => _saveItem(item.index)}>
                            <FontAwesomeIcon icon={faHeart} style={{ fontSize: 16, color: isSaved ? "#ff595e" : "#fff" }} />
                            <div>Save</div>
                        </div> */}
                        <div className='icon_button delete' onClick={() => _onDelete(_item.id)}>
                            <FontAwesomeIcon icon={faTrash} style={{ fontSize: 16, color: "#fff" }} />
                            <div>Delete</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}