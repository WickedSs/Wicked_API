import { useRef, createRef } from 'react'
import API_CALLS from '../../app/api/api_routes';


export default function InvoiceGenerator({ _invoiceState }) {
    
    const input_refs = useRef([createRef(), createRef(), createRef(), createRef()]);
    const { invoice, setInvoice } = _invoiceState

    const _generate_invoice = async (id) => {
        let ivnoice_pdf_response = await API_CALLS.REQUEST_FILE("invoice", "request", id, "NoName-M01", 3101);
        console.log(ivnoice_pdf_response);
        if (ivnoice_pdf_response?.status !== undefined) {
            const file = new Blob([ivnoice_pdf_response.data], { type: "application/pdf" });
            const fileURL = URL.createObjectURL(file);
            const pdfWindow = window.open();
            pdfWindow.location.href = fileURL; 
        } else {
            console.log(ivnoice_pdf_response);
        }
    }

    return (
            <div className="invoice_generator">
                <div className="hbox_detail po_podate">
                    <div className="vbox invoice_number">
                        <label htmlFor="OrderNumberInput" style={{ marginBottom: 5 }}>Order Number</label>
                        <input name="OrderNumber" type="text" id="OrderNumberInput"
                            // placeholder="Invoice Order Number"
                            ref={input_refs[0]}
                            value={_invoiceState.invoice.purchase_order}
                            // onChange={(e) => setBarcode(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key == "Enter") {
                                    _invoiceState.setInvoice((prevState) => ({...prevState, purchase_order: e.target.value }));
                                }
                            }}
                        />
                    </div>
                    <div className="vbox product_barcode">
                        <label htmlFor="orderDateInput" style={{ marginBottom: 5 }}>Order Date</label>
                        <input name="order" type="text" id="orderDateInput"
                            // placeholder="Invoice Order Date"
                            ref={input_refs[1]}
                            value={_invoiceState.invoice.purchase_order_date}
                            // onChange={(e) => setBarcode(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key == "Enter") {
                                    _invoiceState.setInvoice((prevState) => ({...prevState, purchase_order_date: e.target.value }));
                                }
                            }}
                        />
                    </div>
                </div>
                <div className="hbox_detail po_podate">
                    <div className="vbox invoice_number">
                        <label htmlFor="deliveryNumberInput" style={{ marginBottom: 5 }}>Delivery Number</label>
                        <input name="deliveryNumber" type="text" id="deliveryNumberInput"
                            // placeholder="Invoice Delivery Number"
                            ref={input_refs[2]}
                            value={_invoiceState.invoice.purchase_form}
                            // onChange={(e) => setBarcode(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key == "Enter") {
                                    _invoiceState.setInvoice((prevState) => ({...prevState, purchase_form: e.target.value }));
                                }
                            }}
                        />
                    </div>
                    <div className="vbox product_barcode">
                        <label htmlFor="deliveryDateInput" style={{ marginBottom: 5 }}>Delivery Date</label>
                        <input name="deliveryDate" type="text" id="deliveryDateInput"
                            // placeholder="Invoice Delivery Date"
                            ref={input_refs[3]}
                            value={_invoiceState.invoice.purchase_form_date}
                            //onChange={(e) => setBarcode(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key == "Enter") {
                                    _invoiceState.setInvoice((prevState) => ({...prevState, purchase_form_date: e.target.value }));
                                }
                            }}
                        />
                    </div>
                </div>
                <div className='total'>
                    <button>Delete Invoice</button>
                    <button onClick={() => _generate_invoice(invoice.id)}>Generate Invoice</button>
                </div>
            </div>
    )
}