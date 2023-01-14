import constant from "../../constants";

export default function InvoiceDetails({ _invoiceState }) {
    return (
            <div className="invoice_details">
                <div className="hbox_detail po_podate">
                    <div className="vbox invoice_number">
                        <label htmlFor="OrderNumberInput" style={{ marginBottom: 5 }}>Invoice Total</label>
                        <input name="OrderNumber" type="text" id="OrderNumberInput"
                            disabled={true}
                            value={constant.formatter(_invoiceState.invoice.invoice_total)}
                            onChange={(e) => _invoiceState.setInvoice((prevState) => ({...prevState, purchase_order: e.target.value }) )}
                            onKeyDown={(e) => {}}
                        />
                    </div>
                    <div className="vbox product_barcode">
                        <label htmlFor="orderDateInput" style={{ marginBottom: 5 }}>Amount Paid</label>
                        <input name="order" type="text" id="orderDateInput"
                            disabled={true}
                            value={constant.formatter(_invoiceState.invoice.amount_paid)}
                            onChange={(e) => _invoiceState.setInvoice((prevState) => ({...prevState, purchase_order_date: e.target.value }))}
                        />
                    </div>
                </div>
                <div className="hbox_detail po_podate">
                    <div className="vbox invoice_number">
                        <label htmlFor="OrderNumberInput" style={{ marginBottom: 5 }}>Invoice Number</label>
                        <input name="OrderNumber" type="text" id="OrderNumberInput"
                            value={_invoiceState.invoice.invoice_number}
                            onChange={(e) => _invoiceState.setInvoice((prevState) => ({...prevState, invoice_number: e.target.value }))}
                        />
                    </div>
                    <div className="vbox product_barcode">
                        <label htmlFor="orderDateInput" style={{ marginBottom: 5 }}>Invoice Date</label>
                        <input name="order" type="text" id="orderDateInput"
                            value={_invoiceState.invoice.operation_date}
                            onChange={(e) => _invoiceState.setInvoice((prevState) => ({...prevState, operation_date: e.target.value }))}
                        />
                    </div>
                </div>
            </div>
    )
}