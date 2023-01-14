import constant from "../../constants"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircle, faEdit, faTrash, faCreditCard, faFileInvoiceDollar } from "@fortawesome/free-solid-svg-icons";

export default function InvoiceRecord({ item, index, _onOpen, _onClose }) {
    return (
        <div className="invoice_record">
            <div className="hbox hashtag">
                <FontAwesomeIcon icon={faFileInvoiceDollar} style={{ fontSize: 20, color: "#AB9AFE" }} />
            </div>
            <div className="hbox buyer_name">
                <div>Buyer Name</div>
                <div>{item.buyer_name}</div>
            </div>
            <div className="hbox operaton_date">
                <div>Date</div>
                <div>{item.operation_date}</div>
            </div>
            <div className="hbox invoice_number">
                <div>Invoice Number</div>
                <div>{item.invoice_number}</div>
            </div>
            <div className="hbox invoice_total">
                <div>Invoice Amount</div>
                <div style={{ color: "#63B4FF" }}>{constant.formatter(item.invoice_total)}</div>
            </div>
            <div className="hbox invoice_paid">
                <div>Amount Paid</div>
                <div style={{ color: "#B1D298" }}>{constant.formatter(item.amount_paid)}</div>
            </div>
            <div className="hbox invoice_remaining">
                <div>Amount Remaining</div>
                <div style={{ color: "#C74C76" }}>{constant.formatter(item.amount_remaining)}</div>
            </div>
            <div className="invoice_pay" onClick={() => _onOpen(item.id, item)}>
                <div>OPEN</div>
            </div>
        </div>
    )
}