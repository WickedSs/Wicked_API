import Image from "next/image"
import {createRef, useEffect, useState} from "react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft, faFloppyDisk, } from "@fortawesome/free-solid-svg-icons";

import NewItem from "../../components/Invoices/invoice_new_item";
import InvoiceGenerator from "../../components/Invoices/invoice_generator";
import InvoiceRecord from "../../components/Invoices/invoice_record";
import InvoiceDetails from "../../components/Invoices/invoice_details";
import InvoiceItemRecord from "../../components/Invoices/invoiceItem_record";
import API_CALLS from '../api/api_routes';
import constant from "../../constants";
import '../../styles/invoices.css';



function InvoiceList({ _currentTradeRegistry, _onOpen }) {
    
    const [searchValue, setSearchValue] = useState("");
    const [currentInvoices, setCurrentInvoices] = useState([]);

    useEffect(() => {
        const fetch_invoices = async () => {
            let _registry = constant.registries[_currentTradeRegistry].replace(/ /g, "_");
            const response = await API_CALLS.SELECT("invoice", "registry", _registry, 3101);
            if (response?.status !== undefined) {
                setCurrentInvoices(response.data);
            } else {
                setCurrentInvoices([]);
            }
        }
        fetch_invoices();
    }, [_currentTradeRegistry]);

    return (
        <div>
            <div className="top_area">
                <div className="vbox invoice_search">
                    <label htmlFor="searchInput" style={{ marginBottom: 5 }}>Search</label>
                    <input name="search" type="text" id="searchInput" placeholder="Search by name ..." value={searchValue}
                        onChange={(e) => setSearchValue(e.target.value)} onKeyDown={() => _pick_item()}
                    />
                </div>
            </div>
            <div className="middle_area">
                { currentInvoices.map((invoice, index) => 
                    <InvoiceRecord key={invoice.id} item={invoice} index={index} _onOpen={_onOpen} /> 
                )}
            </div>
        </div>
    )
}


function InvoiceItemList({ _invoiceState, _onClose }) {
    
    const newBarcodeRef = createRef(), newQuantityRef = createRef(), saveRef = createRef();
    const [currentInvoiceItems, setCurrentInvoiceItems] = useState([]);
    const [isChanged, setChanged] = useState(false);
    const { invoice, setInvoice } = _invoiceState;
    
    useEffect(() => {
        const fetch_invoices = async () => {
            const response = await API_CALLS.SELECT("invoiceItem", "identifier", invoice.invoice_identifier, 3102);
            setCurrentInvoiceItems(response.data);
        }
        fetch_invoices();
    }, []);

    const _onSaveClick = async () => {
        let update_response = await API_CALLS.UPDATE("invoice", undefined, invoice.id, invoice, 3101);
        if (update_response?.status !== undefined) {
            setChanged(false);
        }
    }

    return (
        <div className="invoice_list_item">
            <div className="invoice_title" style={{ justifyContent: isChanged ? "space-between" : "flex-start" }}>
                <div onClick={() => _onClose(0)} style={{ marginRight: isChanged ? "0em" : "1em" }} >
                    <FontAwesomeIcon icon={faArrowLeft} style={{ fontSize: 32, color: "white" }} />
                </div>
                <div>
                    <span style={{ color: "#957fef"}}>{invoice.buyer_name}</span>
                    <span>'s invoice</span>
                </div>
                {
                    isChanged && (
                        <div className="save_on_edit" ref={saveRef} onClick={(e) => _onSaveClick()}>
                            <FontAwesomeIcon icon={faFloppyDisk} style={{ fontSize: 32, color: "white" }} />
                        </div>
                    )
                }
            </div>
            <NewItem _invoice={_invoiceState} _currentInvoiceItems={{ currentInvoiceItems, setCurrentInvoiceItems }} _changed={{ isChanged, setChanged }} />
            <div className="middle_area">
                { currentInvoiceItems.map((item, index) => 
                    <InvoiceItemRecord key={item.id} 
                        _item={item} _invoiceState={_invoiceState}
                        _invoiceItems={{ currentInvoiceItems, setCurrentInvoiceItems }}
                        _changed = {{ isChanged, setChanged }}
                    /> 
                )}
            </div>
        </div>
    )
}


export default function Invoices({ _currentTradeRegistry }) {
    const [invoiceOpen, setInvoiceOpen] = useState(false);
    const [invoice, setInvoice] = useState({});

    const _on_open = (index, item) => {
        setInvoice(item);
        setInvoiceOpen(true);
    }
    const _on_close = (index) => setInvoiceOpen(false);
    const _generate_invoice = () => {};


    return (
        <div className="invoice_scene">
            <div className='invoice_left_side' style={{ width: invoiceOpen ? "47vw" : "calc(47vw + 34vw)" }}>
                { !invoiceOpen && ( <InvoiceList _currentTradeRegistry={_currentTradeRegistry} _onOpen={_on_open} /> )}
                { invoiceOpen && ( <InvoiceItemList _invoiceState={{ invoice, setInvoice }} _onClose={_on_close} />) }
            </div>
            <div className='invoice_right_side' style={{ display: invoiceOpen ? "flex" : "none" }}>
                <InvoiceDetails _invoiceState={{ invoice, setInvoice }} />
                <InvoiceGenerator _invoiceState={{ invoice, setInvoice }} />
            </div>
        </div>
    )
}